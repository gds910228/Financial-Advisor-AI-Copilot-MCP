"""
Basic Workflow Example for Financial Advisor AI Copilot MCP Service

This script demonstrates a complete workflow from client onboarding to report generation.
"""

import asyncio
import json
from datetime import datetime, timedelta

# Simulated MCP client calls (in real usage, these would be MCP tool calls)
class MCPClient:
    """Simulated MCP client for demonstration purposes"""
    
    def __init__(self):
        self.tools = {}
    
    async def call_tool(self, tool_name: str, **kwargs):
        """Simulate MCP tool call"""
        print(f"🔧 Calling tool: {tool_name}")
        print(f"📝 Parameters: {json.dumps(kwargs, indent=2)}")
        
        # Simulate tool execution time
        await asyncio.sleep(0.5)
        
        # Return simulated responses based on tool name
        if tool_name == "create_client_profile":
            return f"✅ Client profile created for {kwargs['name']} with {kwargs['risk_tolerance']} risk tolerance and ${kwargs['capital']:,.2f} capital"
        
        elif tool_name == "build_portfolio":
            return {
                "status": "success",
                "portfolio": {
                    "assets": {
                        "VTI": 0.40,  # US Total Stock Market
                        "VEA": 0.25,  # Developed Markets
                        "VWO": 0.15,  # Emerging Markets
                        "BND": 0.15,  # US Total Bond Market
                        "VNQ": 0.05   # Real Estate
                    },
                    "expected_return": 0.078,
                    "volatility": 0.142,
                    "sharpe_ratio": 0.55
                },
                "client_profile": kwargs
            }
        
        elif tool_name == "get_market_data":
            return {
                "status": "success",
                "data": {
                    "VTI": {
                        "current_price": 245.67,
                        "price_change_pct": 12.34,
                        "volume": 3456789,
                        "market_cap": "1.2T",
                        "sector": "Diversified",
                        "pe_ratio": 21.5
                    },
                    "VEA": {
                        "current_price": 52.18,
                        "price_change_pct": 8.92,
                        "volume": 2345678,
                        "market_cap": "850B",
                        "sector": "International",
                        "pe_ratio": 15.2
                    }
                }
            }
        
        elif tool_name == "backtest_portfolio":
            return {
                "status": "success",
                "backtest_results": {
                    "period": f"{kwargs.get('start_date', '2020-01-01')} to {kwargs.get('end_date', '2024-01-01')}",
                    "total_return": 0.456,
                    "cagr": 0.098,
                    "volatility": 0.145,
                    "sharpe_ratio": 0.68,
                    "max_drawdown": -0.187
                },
                "portfolio": kwargs["portfolio"]
            }
        
        elif tool_name == "adjust_portfolio":
            return {
                "status": "success",
                "original_portfolio": kwargs["current_portfolio"],
                "adjusted_portfolio": {
                    "VTI": 0.35,
                    "VEA": 0.25,
                    "VWO": 0.15,
                    "BND": 0.10,
                    "VNQ": 0.05,
                    "QQQ": 0.10  # Added tech allocation
                },
                "adjustment_description": kwargs["adjustments"]
            }
        
        elif tool_name == "generate_investment_report":
            return f"""
INVESTMENT ADVISORY REPORT
==========================

Client: {kwargs.get('client_name', 'Demo Client')}
Date: {datetime.now().strftime('%Y-%m-%d')}

CLIENT PROFILE
--------------
Risk Tolerance: Moderate
Investment Horizon: 15 years
Available Capital: $500,000.00

RECOMMENDED PORTFOLIO ALLOCATION
--------------------------------
VTI (US Total Market): 35.0%
VEA (Developed Markets): 25.0%
VWO (Emerging Markets): 15.0%
BND (US Bonds): 10.0%
VNQ (Real Estate): 5.0%
QQQ (Technology): 10.0%

PORTFOLIO RATIONALE
-------------------
This diversified portfolio balances growth potential with risk management,
suitable for a moderate risk profile with a 15-year investment horizon.

PERFORMANCE EXPECTATIONS
------------------------
Expected Annual Return: 7.8%
Expected Volatility: 14.2%
Sharpe Ratio: 0.55

This report is for demonstration purposes only.
"""
        
        return {"status": "success", "message": "Tool executed successfully"}

async def demonstrate_basic_workflow():
    """Demonstrate a complete financial advisory workflow"""
    
    print("🚀 Financial Advisor AI Copilot - Basic Workflow Demo")
    print("=" * 60)
    
    client = MCPClient()
    
    # Step 1: Create Client Profile
    print("\n📋 Step 1: Creating Client Profile")
    print("-" * 40)
    
    profile_result = await client.call_tool(
        "create_client_profile",
        name="Sarah Johnson",
        age=35,
        risk_tolerance="moderate",
        investment_horizon=15,
        capital=500000.0,
        esg_preference=True,
        sector_preferences=["Technology", "Healthcare"]
    )
    print(f"Result: {profile_result}")
    
    # Step 2: Build Initial Portfolio
    print("\n🏗️ Step 2: Building Initial Portfolio")
    print("-" * 40)
    
    portfolio_result = await client.call_tool(
        "build_portfolio",
        client_name="Sarah Johnson"
    )
    print(f"Result: {json.dumps(portfolio_result, indent=2)}")
    
    # Step 3: Get Market Data
    print("\n📊 Step 3: Fetching Market Data")
    print("-" * 40)
    
    portfolio_assets = list(portfolio_result["portfolio"]["assets"].keys())
    market_data = await client.call_tool(
        "get_market_data",
        symbols=portfolio_assets[:2],  # Just first 2 for demo
        period="1y"
    )
    print(f"Result: {json.dumps(market_data, indent=2)}")
    
    # Step 4: Backtest Portfolio
    print("\n📈 Step 4: Backtesting Portfolio Performance")
    print("-" * 40)
    
    backtest_result = await client.call_tool(
        "backtest_portfolio",
        portfolio=portfolio_result["portfolio"]["assets"],
        start_date="2020-01-01",
        end_date="2024-01-01"
    )
    print(f"Result: {json.dumps(backtest_result, indent=2)}")
    
    # Step 5: Adjust Portfolio
    print("\n🔧 Step 5: Adjusting Portfolio Based on Preferences")
    print("-" * 40)
    
    adjustment_result = await client.call_tool(
        "adjust_portfolio",
        client_name="Sarah Johnson",
        current_portfolio=portfolio_result["portfolio"]["assets"],
        adjustments="increase tech allocation by 10% and reduce bonds slightly"
    )
    print(f"Result: {json.dumps(adjustment_result, indent=2)}")
    
    # Step 6: Generate Final Report
    print("\n📄 Step 6: Generating Investment Report")
    print("-" * 40)
    
    report = await client.call_tool(
        "generate_investment_report",
        client_name="Sarah Johnson",
        portfolio=adjustment_result["adjusted_portfolio"]
    )
    print(f"Result:\n{report}")
    
    print("\n✅ Workflow Complete!")
    print("=" * 60)
    print("This demonstrates the complete end-to-end process:")
    print("1. Client onboarding and profile creation")
    print("2. AI-powered portfolio construction")
    print("3. Real-time market data integration")
    print("4. Historical performance backtesting")
    print("5. Natural language portfolio adjustments")
    print("6. Professional report generation")

if __name__ == "__main__":
    asyncio.run(demonstrate_basic_workflow())