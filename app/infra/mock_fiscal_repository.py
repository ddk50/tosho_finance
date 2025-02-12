from app.domain.finalcial_data import FiscalData, PLData, BSData
from app.repository.financial_repository import FiscalReportRepository


class MockFiscalReportRepository(FiscalReportRepository):
    def fetch(self, ticket_symbol: str, company_name: str) -> FiscalData:
        return FiscalData(
            pl=PLData(
                revenue=1000000.0,
                cost_of_goods_sold=400000.0,
                gross_profit=600000.0,
                selling_general_admin_expenses=200000.0,
                operating_profit=400000.0,
                non_operating_income=50000.0,
                non_operating_expenses=30000.0,
                ordinary_profit=420000.0,
                extraordinary_income=20000.0,
                extraordinary_losses=10000.0,
                profit_before_tax=430000.0,
                corporate_taxes=100000.0,
                net_profit=330000.0,
            ),
            bs=BSData(
                current_assets=1500000.0,
                cash_and_cash_equivalents=500000.0,
                accounts_receivable=400000.0,
                inventory=300000.0,
                fixed_assets=2000000.0,
                tangible_fixed_assets=1500000.0,
                intangible_fixed_assets=300000.0,
                investments_other_assets=200000.0,
                current_liabilities=1000000.0,
                accounts_payable=400000.0,
                short_term_loans_payable=300000.0,
                non_current_liabilities=1200000.0,
                bonds_payable=500000.0,
                long_term_loans_payable=700000.0,
                net_assets=1300000.0,
                capital_stock=500000.0,
                retained_earnings=800000.0,
            )
        )
