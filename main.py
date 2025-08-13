"""
Financial Advisor AI Copilot MCP Service

A comprehensive MCP service for financial analysts providing intelligent investment advisory capabilities.
"""

from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Any
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# Create MCP server
mcp = FastMCP("Financial Advisor AI Copilot")

# Data Models
class ClientProfile(BaseModel):
    """Client investment profile"""
    name: str
    age: int
    risk_tolerance: str = Field(..., description="conservative, moderate, aggressive")
    investment_horizon: int = Field(..., description="Investment horizon in years")
    capital: float = Field(..., description="Available capital for investment")
    esg_preference: bool = Field(default=False, description="ESG investment preference")
    sector_preferences: List[str] = Field(default=[], description="Preferred sectors")

class PortfolioAllocation(BaseModel):
    """Portfolio allocation model"""
    assets: Dict[str, float] = Field(..., description="Asset symbol to weight mapping")
    expected_return: float = Field(..., description="Expected annual return")
    volatility: float = Field(..., description="Portfolio volatility")
    sharpe_ratio: float = Field(..., description="Sharpe ratio")

class BacktestResult(BaseModel):
    """Backtesting results"""
    cagr: float = Field(..., description="Compound Annual Growth Rate")
    max_drawdown: float = Field(..., description="Maximum drawdown")
    sharpe_ratio: float = Field(..., description="Sharpe ratio")
    volatility: float = Field(..., description="Annual volatility")
    total_return: float = Field(..., description="Total return over period")

# Global storage for client profiles (in production, use proper database)
client_profiles: Dict[str, ClientProfile] = {}

@mcp.tool()
def create_client_profile(
    name: str,
    age: int,
    risk_tolerance: str,
    investment_horizon: int,
    capital: float,
    esg_preference: bool = False,
    sector_preferences: List[str] = None
) -> str:
    """Create a new client investment profile"""
    if sector_preferences is None:
        sector_preferences = []
    
    profile = ClientProfile(
        name=name,
        age=age,
        risk_tolerance=risk_tolerance,
        investment_horizon=investment_horizon,
        capital=capital,
        esg_preference=esg_preference,
        sector_preferences=sector_preferences
    )
    
    client_profiles[name] = profile
    return f"Client profile created for {name} with {risk_tolerance} risk tolerance and ${capital:,.2f} capital"

@mcp.tool()
def get_market_data(symbols: List[str], period: str = "1y") -> Dict[str, Any]:
    """Retrieve market data for given symbols"""
    try:
        data = {}
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period=period)
            info = ticker.info
            
            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                price_change = ((current_price - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
                
                data[symbol] = {
                    "current_price": float(current_price),
                    "price_change_pct": float(price_change),
                    "volume": int(hist['Volume'].iloc[-1]),
                    "market_cap": info.get('marketCap', 'N/A'),
                    "sector": info.get('sector', 'N/A'),
                    "pe_ratio": info.get('trailingPE', 'N/A')
                }
        
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def build_portfolio(client_name: str, asset_universe: List[str] = None) -> Dict[str, Any]:
    """Build an optimized portfolio for a client based on their profile"""
    if client_name not in client_profiles:
        return {"status": "error", "message": f"Client profile not found for {client_name}"}
    
    profile = client_profiles[client_name]
    
    # Default asset universe if not provided
    if asset_universe is None:
        if profile.risk_tolerance == "conservative":
            asset_universe = ["BND", "VTI", "VEA", "VWO"]  # Bonds, US stocks, International
        elif profile.risk_tolerance == "moderate":
            asset_universe = ["VTI", "VEA", "VWO", "BND", "VNQ"]  # Balanced mix
        else:  # aggressive
            asset_universe = ["VTI", "VEA", "VWO", "VNQ", "QQQ"]  # Growth focused
    
    try:
        # Fetch historical data for portfolio optimization
        data = yf.download(asset_universe, period="2y", progress=False)['Adj Close']
        returns = data.pct_change().dropna()
        
        # Simple risk-based allocation (in production, use proper optimization)
        n_assets = len(asset_universe)
        
        if profile.risk_tolerance == "conservative":
            # Higher allocation to bonds/stable assets
            weights = np.array([0.4, 0.3, 0.2, 0.1] + [0.0] * (n_assets - 4))[:n_assets]
        elif profile.risk_tolerance == "moderate":
            # Balanced allocation
            weights = np.array([1.0 / n_assets] * n_assets)
        else:  # aggressive
            # Higher allocation to growth assets
            weights = np.array([0.4, 0.25, 0.2, 0.1, 0.05] + [0.0] * (n_assets - 5))[:n_assets]
        
        # Normalize weights
        weights = weights / weights.sum()
        
        # Calculate portfolio metrics
        portfolio_return = np.sum(returns.mean() * weights) * 252
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
        sharpe_ratio = portfolio_return / portfolio_volatility if portfolio_volatility > 0 else 0
        
        allocation = dict(zip(asset_universe, weights))
        
        return {
            "status": "success",
            "portfolio": {
                "assets": {k: float(v) for k, v in allocation.items()},
                "expected_return": float(portfolio_return),
                "volatility": float(portfolio_volatility),
                "sharpe_ratio": float(sharpe_ratio)
            },
            "client_profile": profile.dict()
        }
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def adjust_portfolio(
    client_name: str,
    current_portfolio: Dict[str, float],
    adjustments: str
) -> Dict[str, Any]:
    """Adjust portfolio based on natural language instructions"""
    if client_name not in client_profiles:
        return {"status": "error", "message": f"Client profile not found for {client_name}"}
    
    try:
        # Simple adjustment logic (in production, use NLP)
        adjusted_portfolio = current_portfolio.copy()
        
        # Parse basic adjustment commands
        if "increase" in adjustments.lower() and "tech" in adjustments.lower():
            # Increase tech allocation
            tech_symbols = ["QQQ", "VGT", "AAPL", "MSFT", "GOOGL"]
            for symbol in tech_symbols:
                if symbol in adjusted_portfolio:
                    adjusted_portfolio[symbol] *= 1.2
        
        if "reduce" in adjustments.lower() and "bond" in adjustments.lower():
            # Reduce bond allocation
            bond_symbols = ["BND", "AGG", "TLT"]
            for symbol in bond_symbols:
                if symbol in adjusted_portfolio:
                    adjusted_portfolio[symbol] *= 0.8
        
        # Normalize weights
        total_weight = sum(adjusted_portfolio.values())
        if total_weight > 0:
            adjusted_portfolio = {k: v/total_weight for k, v in adjusted_portfolio.items()}
        
        return {
            "status": "success",
            "original_portfolio": current_portfolio,
            "adjusted_portfolio": adjusted_portfolio,
            "adjustment_description": adjustments
        }
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def backtest_portfolio(
    portfolio: Dict[str, float],
    start_date: str = "2020-01-01",
    end_date: str = None
) -> Dict[str, Any]:
    """Backtest portfolio performance over specified period"""
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    try:
        symbols = list(portfolio.keys())
        weights = np.array(list(portfolio.values()))
        
        # Download historical data
        data = yf.download(symbols, start=start_date, end=end_date, progress=False)['Adj Close']
        returns = data.pct_change().dropna()
        
        # Calculate portfolio returns
        portfolio_returns = (returns * weights).sum(axis=1)
        cumulative_returns = (1 + portfolio_returns).cumprod()
        
        # Calculate metrics
        total_return = float(cumulative_returns.iloc[-1] - 1)
        cagr = float((cumulative_returns.iloc[-1] ** (252 / len(portfolio_returns))) - 1)
        volatility = float(portfolio_returns.std() * np.sqrt(252))
        sharpe_ratio = float(cagr / volatility) if volatility > 0 else 0
        
        # Calculate maximum drawdown
        rolling_max = cumulative_returns.expanding().max()
        drawdown = (cumulative_returns - rolling_max) / rolling_max
        max_drawdown = float(drawdown.min())
        
        return {
            "status": "success",
            "backtest_results": {
                "period": f"{start_date} to {end_date}",
                "total_return": total_return,
                "cagr": cagr,
                "volatility": volatility,
                "sharpe_ratio": sharpe_ratio,
                "max_drawdown": max_drawdown
            },
            "portfolio": portfolio
        }
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def generate_investment_report(client_name: str, portfolio: Dict[str, float]) -> str:
    """Generate a comprehensive investment report for the client"""
    if client_name not in client_profiles:
        return f"Error: Client profile not found for {client_name}"
    
    profile = client_profiles[client_name]
    
    # Generate report content
    report = f"""
INVESTMENT ADVISORY REPORT
==========================

Client: {profile.name}
Date: {datetime.now().strftime('%Y-%m-%d')}

CLIENT PROFILE
--------------
Age: {profile.age}
Risk Tolerance: {profile.risk_tolerance.title()}
Investment Horizon: {profile.investment_horizon} years
Available Capital: ${profile.capital:,.2f}
ESG Preference: {'Yes' if profile.esg_preference else 'No'}

RECOMMENDED PORTFOLIO ALLOCATION
--------------------------------
"""
    
    for symbol, weight in portfolio.items():
        report += f"{symbol}: {weight*100:.1f}%\n"
    
    report += f"""

PORTFOLIO RATIONALE
-------------------
This portfolio allocation is designed to match your {profile.risk_tolerance} risk profile 
and {profile.investment_horizon}-year investment horizon. The diversified approach helps 
balance growth potential with risk management.

NEXT STEPS
----------
1. Review the proposed allocation
2. Discuss any concerns or preferences
3. Implement the investment strategy
4. Schedule regular portfolio reviews

This report is for informational purposes only and does not constitute investment advice.
Please consult with a qualified financial advisor before making investment decisions.
"""
    
    return report

if __name__ == "__main__":
    # Start the MCP server
    mcp.run()