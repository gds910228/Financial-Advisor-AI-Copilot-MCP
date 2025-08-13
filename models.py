#!/usr/bin/env python3
"""
Data models for Financial Advisor AI Copilot
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class ClientProfile(BaseModel):
    """Client profile with investment preferences"""
    name: str = Field(..., description="Client name")
    age: int = Field(..., ge=18, le=100, description="Client age")
    risk_tolerance: str = Field(..., description="Risk tolerance level")
    investment_horizon: int = Field(..., ge=1, description="Investment horizon in years")
    monthly_income: float = Field(..., ge=0, description="Monthly income")
    investment_goals: List[str] = Field(default_factory=list, description="Investment goals")
    existing_assets: Dict[str, float] = Field(default_factory=dict, description="Existing assets")


class PortfolioAllocation(BaseModel):
    """Portfolio allocation with assets and weights"""
    assets: List[str] = Field(..., description="List of asset symbols")
    weights: List[float] = Field(..., description="Asset weights (should sum to 1.0)")
    expected_return: float = Field(..., description="Expected annual return")
    risk_level: str = Field(..., description="Portfolio risk level")
    rebalance_frequency: str = Field(default="quarterly", description="Rebalancing frequency")


class BacktestResult(BaseModel):
    """Backtest results with performance metrics"""
    start_date: datetime = Field(..., description="Backtest start date")
    end_date: datetime = Field(..., description="Backtest end date")
    total_return: float = Field(..., description="Total return over period")
    annual_return: float = Field(..., description="Annualized return")
    volatility: float = Field(..., description="Portfolio volatility")
    sharpe_ratio: float = Field(..., description="Sharpe ratio")
    max_drawdown: float = Field(..., description="Maximum drawdown")
    portfolio_value: List[float] = Field(default_factory=list, description="Portfolio value over time")
    benchmark_return: float = Field(..., description="Benchmark return for comparison")


class MarketData(BaseModel):
    """Market data for a single asset"""
    symbol: str = Field(..., description="Asset symbol")
    price: float = Field(..., description="Current price")
    change: float = Field(..., description="Price change")
    change_percent: float = Field(..., description="Price change percentage")
    volume: int = Field(..., description="Trading volume")
    timestamp: datetime = Field(..., description="Data timestamp")


class InvestmentRecommendation(BaseModel):
    """Investment recommendation with rationale"""
    action: str = Field(..., description="Recommended action (buy/sell/hold)")
    asset: str = Field(..., description="Asset symbol")
    quantity: float = Field(..., description="Recommended quantity")
    rationale: str = Field(..., description="Reasoning for recommendation")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score")
    risk_assessment: str = Field(..., description="Risk assessment")