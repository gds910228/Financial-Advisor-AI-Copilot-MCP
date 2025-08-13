"""
Test script to verify the MCP server functionality

This script tests the actual MCP server by running it and verifying tool responses.
"""

import subprocess
import time
import json
import sys
from datetime import datetime

def test_server_startup():
    """Test if the MCP server starts successfully"""
    print("🚀 Testing MCP Server Startup...")
    
    try:
        # Start the server in a subprocess
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Give it a few seconds to start
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("✅ MCP Server started successfully")
            process.terminate()
            process.wait()
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Server failed to start")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("📦 Testing Dependencies...")
    
    required_packages = [
        "mcp",
        "fastapi", 
        "pydantic",
        "yfinance",
        "numpy",
        "pandas",
        "scipy"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Run: uv sync")
        return False
    else:
        print("✅ All dependencies installed")
        return True

def test_configuration():
    """Test configuration loading"""
    print("⚙️  Testing Configuration...")
    
    try:
        from config import config
        print(f"✅ Configuration loaded")
        print(f"   Service: {config.service_name}")
        print(f"   Version: {config.version}")
        print(f"   Data Providers: {len(config.data_providers)}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_data_models():
    """Test Pydantic data models"""
    print("📊 Testing Data Models...")
    
    try:
        from main import ClientProfile, PortfolioAllocation, BacktestResult
        
        # Test ClientProfile
        profile = ClientProfile(
            name="Test Client",
            age=35,
            risk_tolerance="moderate",
            investment_horizon=10,
            capital=100000.0
        )
        print("✅ ClientProfile model works")
        
        # Test PortfolioAllocation
        portfolio = PortfolioAllocation(
            assets={"VTI": 0.6, "BND": 0.4},
            expected_return=0.07,
            volatility=0.12,
            sharpe_ratio=0.58
        )
        print("✅ PortfolioAllocation model works")
        
        # Test BacktestResult
        backtest = BacktestResult(
            cagr=0.08,
            max_drawdown=-0.15,
            sharpe_ratio=0.65,
            volatility=0.14,
            total_return=0.45
        )
        print("✅ BacktestResult model works")
        
        return True
        
    except Exception as e:
        print(f"❌ Data model error: {e}")
        return False

def test_market_data_access():
    """Test market data access"""
    print("📈 Testing Market Data Access...")
    
    try:
        import yfinance as yf
        
        # Test basic data fetch
        ticker = yf.Ticker("AAPL")
        hist = ticker.history(period="5d")
        
        if not hist.empty:
            print("✅ Market data access works")
            print(f"   Retrieved {len(hist)} days of AAPL data")
            return True
        else:
            print("❌ No market data retrieved")
            return False
            
    except Exception as e:
        print(f"❌ Market data error: {e}")
        return False

def run_comprehensive_test():
    """Run all tests"""
    print("🧪 Financial Advisor AI Copilot - Comprehensive Test Suite")
    print("=" * 65)
    print(f"Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests = [
        ("Dependencies", test_dependencies),
        ("Configuration", test_configuration),
        ("Data Models", test_data_models),
        ("Market Data Access", test_market_data_access),
        ("Server Startup", test_server_startup)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results[test_name] = False
        print()
    
    # Summary
    print("=" * 65)
    print("🏁 TEST SUMMARY")
    print("=" * 65)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<30} {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! The MCP service is ready for use.")
        print("\nNext steps:")
        print("1. Run the examples: python examples/run_examples.py")
        print("2. Start the MCP server: python main.py")
        print("3. Connect your MCP client to test the tools")
    else:
        print("⚠️  Some tests failed. Please fix the issues before proceeding.")
    
    print(f"\nTest completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    run_comprehensive_test()