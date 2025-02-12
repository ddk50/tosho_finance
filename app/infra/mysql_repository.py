from sqlalchemy.orm import relationship, sessionmaker, Session
from app.repository.financial_repository import FinancialRepository, DBRepository
from app.domain.finalcial_data import FinancialData, FiscalData
from app.model.fiscal_model import CompanyModel, PLDataModel, BSDataModel


class SQLAlchemyRepository(DBRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_fiscal(self, company_name: str, ticker_symbol: str, fiscal_data: FiscalData) -> None:
        try:
            with self.session.begin(): # トランザクションの開始
                company = self.session.query(CompanyModel).filter_by(ticker_symbol=ticker_symbol).one_or_none()

                if not company:
                    company = CompanyModel(name=company_name, ticker_symbol=ticker_symbol)
                    self.session.add(company)
                    self.session.flush()  # company.id を取得するため flush を実行

                pl_data = PLDataModel(company_id=company.id, **vars(fiscal_data.pl))
                bs_data = BSDataModel(company_id=company.id, **vars(fiscal_data.bs))

                self.session.add(pl_data)
                self.session.add(bs_data)
        except Exception as e:
            self.session.rollback()  # エラー発生時はロールバック
            raise e  # 例外を再送出
