from sqlalchemy.orm import sessionmaker
from db.config import engine
from app.repository.financial_repository import FinancialRepository
from app.domain.finalcial_data import FinancialData
from app.infra.models import FinancialDataModel

# SQLAlchemy セッション
Session = sessionmaker(bind=engine)

class MySQLRepository(FinancialRepository):
    """MySQL にデータを保存する具体的な実装"""

    def save(self, data: FinancialData):
        """MySQL に財務データを保存"""
        session = Session()
        record = FinancialDataModel(**data.__dict__)
        session.add(record)
        session.commit()
        session.close()
