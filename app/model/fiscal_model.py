from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RawCompany(Base):
    __tablename__ = 'raw_companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=True, index=True)
    code = Column(String(255), nullable=False, unique=True, index=True)  # ユニーク制約を追加
    name = Column(String(255), nullable=False, index=True)
    market_product = Column(String(255), nullable=False, index=True)
    industry33_code = Column(Integer, nullable=True)
    industry33_category = Column(String(255), nullable=True)
    industry17_code = Column(Integer, nullable=True)
    industry17_category = Column(String(255), nullable=True)
    size_code = Column(Integer, nullable=True)
    size_category = Column(String(255), nullable=True)

    # タイムスタンプの追加
    created_at = Column(DateTime, nullable=False, default=func.now(), index=True)
    modified_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now(), index=True)

    def __repr__(self):
        return f"<RawCompany(code={self.code}, name={self.name})>"

class CompanyModel(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    ticker_symbol = Column(String(255), nullable=False)

    pl_data = relationship(
        "PLDataModel",
        back_populates="company",
        cascade="all, delete-orphan",
        lazy='joined',
        uselist=True
    )

    bs_data = relationship(
        "BSDataModel",
        back_populates="company",
        cascade="all, delete-orphan",
        lazy='joined',
        uselist=True
    )

    # タイムスタンプの追加
    created_at = Column(DateTime, nullable=False, default=func.now())
    modified_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


class PLDataModel(Base):
    __tablename__ = "pl_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    revenue = Column(Float, nullable=True)
    cost_of_goods_sold = Column(Float, nullable=True)
    gross_profit = Column(Float, nullable=True)
    selling_general_admin_expenses = Column(Float, nullable=True)
    operating_profit = Column(Float, nullable=True)
    non_operating_income = Column(Float, nullable=True)
    non_operating_expenses = Column(Float, nullable=True)
    ordinary_profit = Column(Float, nullable=True)
    extraordinary_income = Column(Float, nullable=True)
    extraordinary_losses = Column(Float, nullable=True)
    profit_before_tax = Column(Float, nullable=True)
    corporate_taxes = Column(Float, nullable=True)
    net_profit = Column(Float, nullable=True)

    company = relationship("CompanyModel", back_populates="pl_data")

    # タイムスタンプの追加
    created_at = Column(DateTime, nullable=False, default=func.now())
    modified_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

class BSDataModel(Base):
    __tablename__ = "bs_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    current_assets = Column(Float, nullable=True)
    cash_and_cash_equivalents = Column(Float, nullable=True)
    accounts_receivable = Column(Float, nullable=True)
    inventory = Column(Float, nullable=True)
    fixed_assets = Column(Float, nullable=True)
    tangible_fixed_assets = Column(Float, nullable=True)
    intangible_fixed_assets = Column(Float, nullable=True)
    investments_other_assets = Column(Float, nullable=True)
    current_liabilities = Column(Float, nullable=True)
    accounts_payable = Column(Float, nullable=True)
    short_term_loans_payable = Column(Float, nullable=True)
    non_current_liabilities = Column(Float, nullable=True)
    bonds_payable = Column(Float, nullable=True)
    long_term_loans_payable = Column(Float, nullable=True)
    net_assets = Column(Float, nullable=True)
    capital_stock = Column(Float, nullable=True)
    retained_earnings = Column(Float, nullable=True)

    company = relationship("CompanyModel", back_populates="bs_data")

    # タイムスタンプの追加
    created_at = Column(DateTime, nullable=False, default=func.now())
    modified_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
