"""
Example Runner for Financial Advisor AI Copilot MCP Service

This script runs all example scenarios and provides a comprehensive demonstration.
"""

import asyncio
import sys
import os
from datetime import datetime

# Add parent directory to path to import examples
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

async def run_all_examples():
    """Run all example scenarios"""
    
    print("🎯 Financial Advisor AI Copilot - Complete Demo Suite")
    print("=" * 70)
    print(f"Demo started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Import and run basic workflow
        print("🔄 Running Basic Workflow Example...")
        from basic_workflow import demonstrate_basic_workflow
        await demonstrate_basic_workflow()
        
        print("\n" + "="*50 + "\n")
        
        # Import and run advanced scenarios
        print("🔄 Running Advanced Scenarios Example...")
        from advanced_scenarios import demonstrate_advanced_scenarios
        await demonstrate_advanced_scenarios()
        
        print("\n" + "="*70)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*70)
        
        # Summary
        print("\n📊 DEMO SUMMARY")
        print("-" * 30)
        print("✅ Basic Workflow: Client onboarding → Portfolio construction → Backtesting → Reporting")
        print("✅ Advanced Scenarios: Multi-generational strategies, ESG focus, Crisis testing")
        print("✅ MCP Tool Integration: All 6 core tools demonstrated")
        print("✅ Real-world Use Cases: Conservative retiree, Aggressive young professional")
        print("✅ Risk Management: Stress testing across multiple market conditions")
        
        print(f"\n🕐 Demo completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure you're running this from the examples directory")
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        raise

async def interactive_demo():
    """Interactive demo allowing user to choose scenarios"""
    
    print("🎮 Interactive Demo Mode")
    print("=" * 30)
    print("Choose a demo to run:")
    print("1. Basic Workflow")
    print("2. Advanced Scenarios")
    print("3. All Examples")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                from basic_workflow import demonstrate_basic_workflow
                await demonstrate_basic_workflow()
            elif choice == "2":
                from advanced_scenarios import demonstrate_advanced_scenarios
                await demonstrate_advanced_scenarios()
            elif choice == "3":
                await run_all_examples()
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-4.")
                
        except KeyboardInterrupt:
            print("\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def print_usage():
    """Print usage instructions"""
    print("📖 Usage Instructions")
    print("=" * 30)
    print("To run the examples:")
    print()
    print("1. Basic demo (all examples):")
    print("   python examples/run_examples.py")
    print()
    print("2. Interactive mode:")
    print("   python examples/run_examples.py --interactive")
    print()
    print("3. Individual examples:")
    print("   python examples/basic_workflow.py")
    print("   python examples/advanced_scenarios.py")
    print()
    print("4. With actual MCP server:")
    print("   # Terminal 1: Start MCP server")
    print("   python main.py")
    print("   # Terminal 2: Connect MCP client and run tools")
    print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print_usage()
        elif sys.argv[1] == "--interactive" or sys.argv[1] == "-i":
            asyncio.run(interactive_demo())
        else:
            print(f"❌ Unknown argument: {sys.argv[1]}")
            print_usage()
    else:
        # Run all examples by default
        asyncio.run(run_all_examples())