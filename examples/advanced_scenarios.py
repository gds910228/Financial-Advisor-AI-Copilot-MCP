"""
Advanced Scenarios for Financial Advisor AI Copilot MCP Service

This script demonstrates advanced use cases and edge cases.
"""

import asyncio
import json
from datetime import datetime

class AdvancedMCPClient:
    """Advanced MCP client with more sophisticated responses"""
    
    async def call_tool(self, tool_name: str, **kwargs):
        """Simulate advanced MCP tool calls"""
        print(f"🔧 Advanced Tool Call: {tool_name}")
        print(f"📝 Parameters: {json.dumps(kwargs, indent=2, default=str)}")
        
        await asyncio.sleep(0.3)
        
        if tool_name == "create_client_profile":
            return {
                "status": "success",
                "message": f"Profile created for {kwargs['name']}",
                "profile_id": f"client_{kwargs['name'].lower().replace(' ', '_')}"
            }
        
        elif tool_name == "build_portfolio" and kwargs.get("asset_universe"):
            # Custom asset universe scenario
            custom_assets = kwargs["asset_universe"]
            weights = [1.0 / len(custom_assets)] * len(custom_assets)
            
            return {
                "status": "success",
                "portfolio": {
                    "assets": dict(zip(custom_assets, weights)),
                    "expected_return": 0.085,
                    "volatility": 0.156,
                    "sharpe_ratio": 0.54,
                    "optimization_method": "Equal Weight (Custom Universe)"
                }
            }
        
        elif tool_name == "backtest_portfolio":
            # Simulate different market conditions
            portfolio = kwargs["portfolio"]
            start_date = kwargs.get("start_date", "2020-01-01")
            
            if "2008" in start_date:
                # Financial crisis scenario
                return {
                    "status": "success",
                    "backtest_results": {
                        "period": f"{start_date} to 2010-12-31",
                        "total_return": -0.234,
                        "cagr": -0.089,
                        "volatility": 0.287,
                        "sharpe_ratio": -0.31,
                        "max_drawdown": -0.456,
                        "scenario": "Financial Crisis Period"
                    },
                    "portfolio": portfolio
                }
            elif "2020" in start_date:
                # COVID-19 scenario
                return {
                    "status": "success",
                    "backtest_results": {
                        "period": f"{start_date} to 2023-12-31",
                        "total_return": 0.678,
                        "cagr": 0.145,
                        "volatility": 0.198,
                        "sharpe_ratio": 0.73,
                        "max_drawdown": -0.234,
                        "scenario": "COVID-19 Recovery Period"
                    },
                    "portfolio": portfolio
                }
        
        elif tool_name == "adjust_portfolio":
            adjustments = kwargs["adjustments"].lower()
            current = kwargs["current_portfolio"]
            adjusted = current.copy()
            
            # More sophisticated adjustment logic
            if "esg" in adjustments:
                # Add ESG-focused ETFs
                adjusted["ESGV"] = 0.15
                adjusted["ICLN"] = 0.10
                # Reduce traditional allocations
                for symbol in list(adjusted.keys()):
                    if symbol not in ["ESGV", "ICLN"]:
                        adjusted[symbol] *= 0.85
            
            if "defensive" in adjustments:
                # Increase defensive allocations
                adjusted["VYM"] = adjusted.get("VYM", 0) + 0.15  # Dividend ETF
                adjusted["VTEB"] = adjusted.get("VTEB", 0) + 0.10  # Tax-exempt bonds
            
            # Normalize weights
            total = sum(adjusted.values())
            adjusted = {k: v/total for k, v in adjusted.items()}
            
            return {
                "status": "success",
                "original_portfolio": current,
                "adjusted_portfolio": adjusted,
                "adjustment_description": kwargs["adjustments"],
                "adjustment_rationale": "Portfolio adjusted based on ESG preferences and defensive positioning"
            }
        
        return {"status": "success", "message": "Advanced tool executed"}

async def scenario_conservative_retiree():
    """Scenario: Conservative portfolio for near-retiree"""
    print("\n🏛️ Scenario 1: Conservative Portfolio for Near-Retiree")
    print("=" * 60)
    
    client = AdvancedMCPClient()
    
    # Create conservative client profile
    await client.call_tool(
        "create_client_profile",
        name="Robert Miller",
        age=62,
        risk_tolerance="conservative",
        investment_horizon=8,
        capital=1200000.0,
        esg_preference=False,
        sector_preferences=["Utilities", "Consumer Staples"]
    )
    
    # Build conservative portfolio
    conservative_assets = ["BND", "VTEB", "VYM", "VTI", "VGIT"]
    portfolio = await client.call_tool(
        "build_portfolio",
        client_name="Robert Miller",
        asset_universe=conservative_assets
    )
    
    # Test during financial crisis
    crisis_backtest = await client.call_tool(
        "backtest_portfolio",
        portfolio=portfolio["portfolio"]["assets"],
        start_date="2008-01-01",
        end_date="2010-12-31"
    )
    
    print("✅ Conservative scenario completed")

async def scenario_aggressive_young_professional():
    """Scenario: Aggressive portfolio for young professional"""
    print("\n🚀 Scenario 2: Aggressive Portfolio for Young Professional")
    print("=" * 60)
    
    client = AdvancedMCPClient()
    
    # Create aggressive client profile
    await client.call_tool(
        "create_client_profile",
        name="Alex Chen",
        age=28,
        risk_tolerance="aggressive",
        investment_horizon=35,
        capital=75000.0,
        esg_preference=True,
        sector_preferences=["Technology", "Clean Energy", "Biotechnology"]
    )
    
    # Build aggressive growth portfolio
    growth_assets = ["QQQ", "VGT", "ARKK", "VWO", "ICLN", "XBI"]
    portfolio = await client.call_tool(
        "build_portfolio",
        client_name="Alex Chen",
        asset_universe=growth_assets
    )
    
    # Test during COVID recovery
    covid_backtest = await client.call_tool(
        "backtest_portfolio",
        portfolio=portfolio["portfolio"]["assets"],
        start_date="2020-03-01",
        end_date="2023-12-31"
    )
    
    print("✅ Aggressive scenario completed")

async def scenario_esg_focused_adjustment():
    """Scenario: ESG-focused portfolio adjustment"""
    print("\n🌱 Scenario 3: ESG-Focused Portfolio Adjustment")
    print("=" * 60)
    
    client = AdvancedMCPClient()
    
    # Start with standard portfolio
    standard_portfolio = {
        "VTI": 0.40,
        "VEA": 0.25,
        "VWO": 0.15,
        "BND": 0.15,
        "VNQ": 0.05
    }
    
    # Adjust for ESG preferences
    esg_adjustment = await client.call_tool(
        "adjust_portfolio",
        client_name="ESG Investor",
        current_portfolio=standard_portfolio,
        adjustments="Convert to ESG-focused portfolio with clean energy exposure"
    )
    
    print("✅ ESG adjustment scenario completed")

async def scenario_market_stress_testing():
    """Scenario: Comprehensive stress testing"""
    print("\n📉 Scenario 4: Market Stress Testing")
    print("=" * 60)
    
    client = AdvancedMCPClient()
    
    test_portfolio = {
        "VTI": 0.50,
        "VEA": 0.20,
        "VWO": 0.15,
        "BND": 0.10,
        "REIT": 0.05
    }
    
    # Test multiple crisis periods
    crisis_periods = [
        ("2008-01-01", "2009-12-31", "Financial Crisis"),
        ("2020-02-01", "2020-05-31", "COVID-19 Crash"),
        ("2000-01-01", "2002-12-31", "Dot-com Bubble")
    ]
    
    for start, end, name in crisis_periods:
        print(f"\n🔍 Testing: {name}")
        result = await client.call_tool(
            "backtest_portfolio",
            portfolio=test_portfolio,
            start_date=start,
            end_date=end
        )
    
    print("✅ Stress testing scenario completed")

async def demonstrate_advanced_scenarios():
    """Run all advanced scenarios"""
    print("🎯 Financial Advisor AI Copilot - Advanced Scenarios Demo")
    print("=" * 70)
    
    scenarios = [
        scenario_conservative_retiree,
        scenario_aggressive_young_professional,
        scenario_esg_focused_adjustment,
        scenario_market_stress_testing
    ]
    
    for scenario in scenarios:
        await scenario()
        await asyncio.sleep(1)  # Brief pause between scenarios
    
    print("\n🏆 All Advanced Scenarios Completed!")
    print("=" * 70)
    print("Advanced capabilities demonstrated:")
    print("• Multi-generational investment strategies")
    print("• ESG-focused portfolio construction")
    print("• Crisis period stress testing")
    print("• Dynamic portfolio adjustments")
    print("• Risk-appropriate asset allocation")

if __name__ == "__main__":
    asyncio.run(demonstrate_advanced_scenarios())