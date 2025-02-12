import os

import pandas as pd
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from app.model.fiscal_model import RawCompany

config_path = os.path.abspath("alembic.ini")

print(f"Config Path: {config_path}")  # 確認用

config = configparser.ConfigParser()
read_files = config.read(config_path)  # 読み込んだファイルリストを取得

# 📌 ここで `alembic` セクションが存在するかチェック
if not read_files:
    raise FileNotFoundError(f"Failed to read alembic.ini from {config_path}")
if "alembic" not in config:
    raise KeyError("Section 'alembic' not found in alembic.ini")


DATABASE_URL = config["alembic"]["sqlalchemy.url"]

# データベースエンジンを作成
engine = create_engine(DATABASE_URL)

# セッションの作成
Session = sessionmaker(bind=engine)
session = Session()

# Excelファイルのパス（適宜変更）
EXCEL_FILE = './utils/data_j.xls'

# Excelデータを読み込む
df = pd.read_excel(EXCEL_FILE, dtype=str)  # すべて文字列として読み込む

# カラム名をデータベースの仕様に合わせて変更
df.columns = [
    'date', 'code', 'name', 'market_product',
    'industry33_code', 'industry33_category',
    'industry17_code', 'industry17_category',
    'size_code', 'size_category'
]

# 📌 "-" を `None` に変換
df = df.map(lambda x: None if x == "-" else x)

# 📌 日付を `YYYYMMDD` から `YYYY-MM-DD` に変換（NULL はそのまま）
df['date'] = df['date'].apply(lambda x: datetime.strptime(x, '%Y%m%d').date() if x and x.isdigit() else None)

# テーブルのデータを一旦削除
session.query(RawCompany).delete()
session.commit()
print("既存のデータを削除しました。")

# データを挿入
try:
    for _, row in df.iterrows():
        company = RawCompany(
            date=row['date'],
            code=row['code'],
            name=row['name'],
            market_product=row['market_product'],
            industry33_code=row['industry33_code'],
            industry33_category=row['industry33_category'],
            industry17_code=row['industry17_code'],
            industry17_category=row['industry17_category'],
            size_code=row['size_code'],
            size_category=row['size_category']
        )
        session.add(company)

    # コミット
    session.commit()
    print("データを正常に挿入しました。")

except Exception as e:
    session.rollback()
    print(f"エラーが発生しました: {e}")

finally:
    session.close()
