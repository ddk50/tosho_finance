import unittest
from typing import List

from app.infra.mock_finance_repository import MockFinancialRepository
from app.repository.financial_repository import FinancialData
from app.repository.financial_repository import FinancialRepository

class TestFinancialData(unittest.TestCase):
    def test_financial_data_initialization(self):
        """FinancialData のインスタンス化をテスト"""
        data = FinancialData(
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
        self.assertEqual(data.company_name, "Tesla, Inc.")
        self.assertEqual(data.symbol, "TSLA")
        self.assertEqual(data.revenue, 1000000000.0)
        self.assertEqual(data.net_income, 500000000.0)
        self.assertEqual(data.eps, 2.5)
        self.assertEqual(data.per, 40.0)
        self.assertEqual(data.dividend_yield, 0.0)
        self.assertEqual(data.market_cap, 600000000000.0)
        self.assertEqual(data.stock_price, 650.0)
        self.assertEqual(data.timestamp, "2024-12-10T15:30:00Z")


class TestFinancialRepository(unittest.TestCase):
    def test_fetch_and_get_all(self):
        """データの保存と取得をテスト"""
        api_repository: FinancialRepository = MockFinancialRepository()

        all_data: List[FinancialData] = [
            api_repository.fetch("AAPL", "Apple Inc."),
            api_repository.fetch("AMZN", "Amazon.com, Inc."),
            api_repository.fetch("TSLA", "Tesla, Inc."),
        ]

        self.assertEqual(len(all_data), 3)
        self.assertEqual(all_data[0].company_name, "Apple Inc.")
        self.assertEqual(all_data[1].symbol, "AMZN")

if __name__ == '__main__':
    unittest.main()
