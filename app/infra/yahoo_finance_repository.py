import yfinance as yf
from app.repository.financial_repository import FinancialRepository
from app.domain.finalcial_data import FinancialData
from datetime import datetime


class YahooFinanceRepository(FinancialRepository):
    """Yahoo Finance からデータを取得する実装"""
    def fetch(self, ticker_symbol: str, company_name: str) -> FinancialData:
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        now_data = datetime.now()
        return FinancialData(
            company_name=company_name,
            symbol=ticker_symbol,
            revenue=info.get("totalRevenue", None),
            net_income=info.get("netIncome", None),
            eps=info.get("trailingEps", None),
            per=info.get("trailingPE", None),
            dividend_yield=info.get("dividendYield", None),
            market_cap=info.get("marketCap", None),
            stock_price=info.get("previousClose", None),
            timestamp=now_data.strftime("%Y-%m-%d %H:%M:%S")
        )

