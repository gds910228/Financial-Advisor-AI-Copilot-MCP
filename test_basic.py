#!/usr/bin/env python3
"""
Basic test without external dependencies
"""

def test_imports():
    """Test basic Python imports"""
    try:
        import json
        import datetime
        import typing
        print("✅ Basic Python modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Basic import failed: {e}")
        return False

def test_mcp_import():
    """Test MCP import"""
    try:
        import mcp
        print("✅ MCP module imported successfully")
        return True
    except ImportError as e:
        print(f"❌ MCP import failed: {e}")
        return False

def test_pydantic_import():
    """Test Pydantic import"""
    try:
        from pydantic import BaseModel
        print("✅ Pydantic imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Pydantic import failed: {e}")
        return False

def test_numpy_pandas():
    """Test numpy and pandas"""
    try:
        import numpy as np
        import pandas as pd
        print("✅ NumPy and Pandas imported successfully")
        return True
    except ImportError as e:
        print(f"❌ NumPy/Pandas import failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Basic Dependency Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_mcp_import,
        test_pydantic_import,
        test_numpy_pandas
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All basic tests passed! Ready for full testing once yfinance is installed.")
    else:
        print("⚠️  Some basic dependencies are missing.")