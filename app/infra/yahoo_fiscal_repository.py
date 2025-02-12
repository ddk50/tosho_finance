from yahooquery import Ticker

from app.domain.finalcial_data import FiscalData, PLData, BSData
from app.repository.financial_repository import FiscalReportRepository


class YahooFiscalReportRepository(FiscalReportRepository):
    def fetch(self, ticket_symbol: str, company_name: str) -> FiscalData:
        ticker = Ticker(ticket_symbol)
        financial_data = ticker.financial_data or {}
        balance_sheet = ticker.balance_sheet() or {}

        return FiscalData(
            pl=PLData(
                revenue=financial_data.get("totalRevenue", None),
                cost_of_goods_sold=financial_data.get("costOfRevenue", None),
                gross_profit=financial_data.get("grossProfit", None),
                selling_general_admin_expenses=financial_data.get("sellingGeneralAdministrative", None),
                operating_profit=financial_data.get("operatingIncome", None),
                non_operating_income=financial_data.get("totalOtherIncomeExpenseNet", None),
                non_operating_expenses=None,
                ordinary_profit=financial_data.get("ebit", None),
                extraordinary_income=None,
                extraordinary_losses=None,
                profit_before_tax=financial_data.get("incomeBeforeTax", None),
                corporate_taxes=financial_data.get("incomeTaxExpense", None),
                net_profit=financial_data.get("netIncome", None),
            ),
            bs=BSData(
                current_assets=balance_sheet.get("totalCurrentAssets", None),
                cash_and_cash_equivalents=balance_sheet.get("cash", None),
                accounts_receivable=balance_sheet.get("netReceivables", None),
                inventory=balance_sheet.get("inventory", None),
                fixed_assets=balance_sheet.get("totalAssets", None),
                tangible_fixed_assets=None,
                intangible_fixed_assets=None,
                investments_other_assets=None,
                current_liabilities=balance_sheet.get("totalCurrentLiabilities", None),
                accounts_payable=balance_sheet.get("accountPayable", None),
                short_term_loans_payable=None,
                non_current_liabilities=balance_sheet.get("totalLiab", None),
                bonds_payable=None,
                long_term_loans_payable=None,
                net_assets=balance_sheet.get("totalStockholderEquity", None),
                capital_stock=None,
                retained_earnings=balance_sheet.get("retainedEarnings", None),
            )
        )
