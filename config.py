"""
Configuration settings for Financial Advisor AI Copilot MCP Service
"""

from pydantic import BaseModel
from typing import Dict, List, Optional

class DataProviderConfig(BaseModel):
    """Configuration for data providers"""
    name: str
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    rate_limit: int = 60  # requests per minute
    enabled: bool = True

class PortfolioConfig(BaseModel):
    """Portfolio optimization configuration"""
    risk_free_rate: float = 0.02  # 2% risk-free rate
    rebalancing_frequency: str = "quarterly"  # monthly, quarterly, annually
    min_weight: float = 0.01  # minimum asset weight (1%)
    max_weight: float = 0.40  # maximum asset weight (40%)

class BacktestConfig(BaseModel):
    """Backtesting configuration"""
    default_period: str = "5y"
    benchmark: str = "SPY"  # S&P 500 as default benchmark
    transaction_cost: float = 0.001  # 0.1% transaction cost

class AppConfig(BaseModel):
    """Main application configuration"""
    service_name: str = "Financial Advisor AI Copilot"
    version: str = "1.0.0"
    
    # Data providers
    data_providers: Dict[str, DataProviderConfig] = {
        "yfinance": DataProviderConfig(name="yfinance", enabled=True),
        "alpha_vantage": DataProviderConfig(
            name="alpha_vantage", 
            enabled=False,
            api_key=None  # Set via environment variable
        ),
        "finnhub": DataProviderConfig(
            name="finnhub",
            enabled=False, 
            api_key=None  # Set via environment variable
        )
    }
    
    # Portfolio settings
    portfolio: PortfolioConfig = PortfolioConfig()
    
    # Backtesting settings
    backtest: BacktestConfig = BacktestConfig()
    
    # Asset universe definitions
    asset_universes: Dict[str, List[str]] = {
        "conservative": ["BND", "VTI", "VEA", "VTEB"],
        "moderate": ["VTI", "VEA", "VWO", "BND", "VNQ"],
        "aggressive": ["VTI", "VEA", "VWO", "VNQ", "QQQ", "VGT"],
        "esg": ["ESGV", "VSGX", "ESGU", "SUSL", "ICLN"]
    }

# Global configuration instance
config = AppConfig()