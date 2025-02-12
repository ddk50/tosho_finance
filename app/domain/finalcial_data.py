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

@dataclass
class PLData:
    revenue: Optional[float] = None  # 売上高
    cost_of_goods_sold: Optional[float] = None  # 売上原価
    gross_profit: Optional[float] = None  # 売上総利益
    selling_general_admin_expenses: Optional[float] = None  # 販売費及び一般管理費
    operating_profit: Optional[float] = None  # 営業利益
    non_operating_income: Optional[float] = None  # 営業外収益
    non_operating_expenses: Optional[float] = None  # 営業外費用
    ordinary_profit: Optional[float] = None  # 経常利益
    extraordinary_income: Optional[float] = None  # 特別利益
    extraordinary_losses: Optional[float] = None  # 特別損失
    profit_before_tax: Optional[float] = None  # 税引前当期純利益
    corporate_taxes: Optional[float] = None  # 法人税等
    net_profit: Optional[float] = None  # 当期純利益

@dataclass
class BSData:
    current_assets: Optional[float] = None  # 流動資産
    cash_and_cash_equivalents: Optional[float] = None  # 現金及び現金同等物
    accounts_receivable: Optional[float] = None  # 売掛金
    inventory: Optional[float] = None  # 棚卸資産
    fixed_assets: Optional[float] = None  # 固定資産
    tangible_fixed_assets: Optional[float] = None  # 有形固定資産
    intangible_fixed_assets: Optional[float] = None  # 無形固定資産
    investments_other_assets: Optional[float] = None  # 投資その他の資産
    current_liabilities: Optional[float] = None  # 流動負債
    accounts_payable: Optional[float] = None  # 買掛金
    short_term_loans_payable: Optional[float] = None  # 短期借入金
    non_current_liabilities: Optional[float] = None  # 固定負債
    bonds_payable: Optional[float] = None  # 社債
    long_term_loans_payable: Optional[float] = None  # 長期借入金
    net_assets: Optional[float] = None  # 純資産
    capital_stock: Optional[float] = None  # 資本金
    retained_earnings: Optional[float] = None  # 利益剰余金

@dataclass
class FiscalData:
    pl: PLData
    bs: BSData
