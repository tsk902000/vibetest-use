#!/usr/bin/env python3
"""
Standalone script to run vibetest on Google.com
Usage: python run_vibetest.py
"""

import asyncio
import os
import sys

# Add the current directory to Python path so we can import vibetest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

async def main():
    """Run vibetest with the specified parameters"""
    
    # Check if OPENAI_API_KEY is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY environment variable is required.")
        print("Please set your OpenAI API key:")
        print("  Windows: set OPENAI_API_KEY=your_api_key_here")
        print("  Linux/Mac: export OPENAI_API_KEY=your_api_key_here")
        return 1
    
    try:
        from vibetest.agents import run_pool, summarize_bug_reports
        
        print("🚀 Starting vibetest on https://google.com")
        print("📊 Parameters:")
        print("   - URL: https://google.com")
        print("   - Agents: 1")
        print("   - Headless: False (browsers will be visible)")
        print()
        
        # Run the test
        test_id = await run_pool(
            base_url="https://google.com",
            num_agents=1,
            headless=False
        )
        
        print(f"✅ Test completed! Test ID: {test_id}")
        print()
        
        # Get and display results
        print("📋 Generating results summary...")
        results = summarize_bug_reports(test_id)
        
        print("=" * 60)
        print("🔍 VIBETEST RESULTS")
        print("=" * 60)
        
        if "error" in results:
            print(f"❌ Error: {results['error']}")
            return 1
        
        # Display summary
        print(f"🌐 URL Tested: https://google.com")
        print(f"🤖 Total Agents: {results.get('total_agents', 'N/A')}")
        print(f"✅ Successful Agents: {results.get('successful_agents', 'N/A')}")
        print(f"❌ Failed Agents: {results.get('failed_agents', 'N/A')}")
        
        if 'duration_formatted' in results:
            print(f"⏱️  Duration: {results['duration_formatted']}")
        
        print(f"📊 Overall Status: {results.get('status_emoji', '')} {results.get('overall_status', 'unknown')}")
        print(f"📝 Description: {results.get('status_description', 'No description available')}")
        print(f"🐛 Total Issues: {results.get('total_issues', 0)}")
        
        # Display severity breakdown
        if 'severity_breakdown' in results:
            severity = results['severity_breakdown']
            
            if severity.get('high_severity'):
                print("\n🔴 HIGH SEVERITY ISSUES:")
                for issue in severity['high_severity']:
                    print(f"   • {issue.get('category', 'Unknown')}: {issue.get('description', 'No description')}")
            
            if severity.get('medium_severity'):
                print("\n🟠 MEDIUM SEVERITY ISSUES:")
                for issue in severity['medium_severity']:
                    print(f"   • {issue.get('category', 'Unknown')}: {issue.get('description', 'No description')}")
            
            if severity.get('low_severity'):
                print("\n🟡 LOW SEVERITY ISSUES:")
                for issue in severity['low_severity']:
                    print(f"   • {issue.get('category', 'Unknown')}: {issue.get('description', 'No description')}")
        
        # Display errors if any
        if results.get('errors'):
            print("\n❌ AGENT ERRORS:")
            for error in results['errors']:
                print(f"   • Agent {error.get('agent_id', 'Unknown')}: {error.get('error', 'Unknown error')}")
        
        print("\n" + "=" * 60)
        print("🎉 Vibetest completed successfully!")
        
        return 0
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Make sure vibetest dependencies are installed:")
        print("  pip install -e .")
        return 1
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)