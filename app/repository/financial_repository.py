from abc import ABC, abstractmethod
from app.domain.finalcial_data import FinancialData
from app.domain.finalcial_data import Company
from app.domain.finalcial_data import FiscalData

class FinancialRepository(ABC):
    """データ保存のインターフェース（抽象クラス）"""
    @abstractmethod
    def fetch(self, ticker_symbol: str, company_name: str) -> FinancialData:
        """財務データを保存するメソッド"""
        pass

class CompanyRepository(ABC):
    @abstractmethod
    def get_all_companies(self) -> list[Company]:
        """ターゲットのティッカーシンボル一覧を返す"""
        pass

class FiscalReportRepository(ABC):
    @abstractmethod
    def fetch(self, ticket_symbol: str, company_name: str) -> FiscalData:
        pass

class DBRepository(ABC):
    @abstractmethod
    def save_fiscal(self, company_name: str, ticker_symbol: str, fiscal_data: FiscalData) -> None:
        pass
