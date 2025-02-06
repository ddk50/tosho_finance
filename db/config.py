import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def load_db_config(config_path="db.yml"):
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config["database"]

db_config = load_db_config()
DATABASE_URL = f"{db_config['driver']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}?charset=utf8mb4"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
