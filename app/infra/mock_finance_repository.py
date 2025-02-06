from app.domain.finalcial_data import FinancialData
from app.repository.financial_repository import FinancialRepository
from typing import Dict

class MockFinancialRepository(FinancialRepository):
    """FinancialRepository のモック実装"""

    def __init__(self):
        """事前に固定データを準備"""
        self.mock_data: Dict[str, FinancialData] = {
            "AAPL": FinancialData(
                company_name="Apple Inc.",
                symbol="AAPL",
                revenue=2000000000.0,
                net_income=700000000.0,
                eps=3.2,
                per=30.0,
                dividend_yield=1.2,
                market_cap=2500000000000.0,
                stock_price=150.0,
                timestamp="2024-12-10T15:30:00Z"
            ),
            "AMZN": FinancialData(
                company_name="Amazon.com, Inc.",
                symbol="AMZN",
                revenue=1800000000.0,
                net_income=600000000.0,
                eps=2.8,
                per=35.0,
                dividend_yield=0.8,
                market_cap=1600000000000.0,
                stock_price=3200.0,
                timestamp="2024-12-10T16:30:00Z"
            ),
            "TSLA": FinancialData(
                company_name="Tesla, Inc.",
                symbol="TSLA",
                revenue=1000000000.0,
                net_income=500000000.0,
                eps=2.5,
                per=40.0,
                dividend_yield=0.0,
                market_cap=600000000000.0,
                stock_price=650.0,
                timestamp="2024-12-10T15:30:00Z"
            )
        }

    def fetch(self, ticker_symbol: str, company_name: str) -> FinancialData:
        """指定されたシンボルの財務データを返す（モックデータを利用）"""
        return self.mock_data.get(ticker_symbol, None)
