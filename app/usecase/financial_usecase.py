from app.infra.yahoo_finance_repository import YahooFinanceRepository
from app.repository.financial_repository import FinancialRepository


def fetch_and_save_data():
    repo = MySQLRepository()
    company_repo = MySQLCompanyRepository()
    api: FinancialRepository = YahooFinanceRepository()  # インターフェースとして扱う

    companies = company_repo.get_all_companies()

    for company in companies:
        data = api.fetch(company.ticker_symbol, company.name)
        repo.save(data)

    print("✅ データを保存しました。")
