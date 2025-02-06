from abc import ABC, abstractmethod
from app.domain.finalcial_data import FinancialData
from app.domain.finalcial_data import Company

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
