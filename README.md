## tosho_finance


### マイグレーション
```bash

```

### 東証のデータのseeding

最初の一回だけでいいです

```bash
$ PYTHONPATH=$(pwd) python utils/import_jpx.py
```

### モデル修正後
```bash
# Model修正後にマイグレーションファイルを作る
$ alembic revision --autogenerate -m "Added indexes to RawCompany"

# マイグレーションを適用
$ alembic upgrade head

```