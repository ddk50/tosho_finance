from dataclasses import dataclass
from typing import Optional

@dataclass
class FinancialData:
    company_name: str
    symbol: str
    revenue: Optional[float]
    net_income: Optional[float]
    eps: Optional[float]
    per: Optional[float]
    dividend_yield: Optional[float]
    market_cap: Optional[float]
    stock_price: Optional[float]
    timestamp: str

@dataclass
class Company:
    id: int
    name: str
    ticker_symbol: str
