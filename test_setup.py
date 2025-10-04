#!/usr/bin/env python3
"""
Simple test script to verify the AI Research Insights Platform setup
"""

import os
import sys
import requests
import json
from pathlib import Path

def test_backend_dependencies():
    """Test if backend dependencies are installed"""
    print("Testing backend dependencies...")
    
    try:
        import flask
        import openai
        import flask_cors
        print("✓ Backend dependencies installed")
        return True
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        return False

def test_frontend_dependencies():
    """Test if frontend dependencies are installed"""
    print("Testing frontend dependencies...")
    
    frontend_path = Path("frontend")
    package_json = frontend_path / "package.json"
    node_modules = frontend_path / "node_modules"
    
    if package_json.exists() and node_modules.exists():
        print("✓ Frontend dependencies installed")
        return True
    else:
        print("✗ Frontend dependencies not installed")
        print("  Run: cd frontend && npm install")
        return False

def test_environment_setup():
    """Test environment configuration"""
    print("Testing environment setup...")
    
    env_file = Path("backend/.env")
    env_example = Path("backend/.env.example")
    
    if env_file.exists():
        print("✓ .env file exists")
        
        # Check if OpenAI key is set
        with open(env_file, 'r') as f:
            content = f.read()
            if "OPENAI_API_KEY=your_openai_api_key_here" in content:
                print("⚠ OpenAI API key not configured")
                print("  Please set your OpenAI API key in backend/.env")
                return False
            elif "OPENAI_API_KEY=" in content:
                print("✓ OpenAI API key configured")
                return True
    else:
        print("✗ .env file not found")
        print("  Run: cd backend && cp .env.example .env")
        return False

def test_backend_server():
    """Test if backend server is running"""
    print("Testing backend server...")
    
    try:
        response = requests.get("http://localhost:5000/health", timeout=5)
        if response.status_code == 200:
            print("✓ Backend server is running")
            return True
        else:
            print(f"✗ Backend server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Backend server is not running")
        print("  Run: cd backend && python app.py")
        return False
    except Exception as e:
        print(f"✗ Error testing backend: {e}")
        return False

def test_frontend_server():
    """Test if frontend server is running"""
    print("Testing frontend server...")
    
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print("✓ Frontend server is running")
            return True
        else:
            print(f"✗ Frontend server returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ Frontend server is not running")
        print("  Run: cd frontend && npm start")
        return False
    except Exception as e:
        print(f"✗ Error testing frontend: {e}")
        return False

def test_api_endpoints():
    """Test API endpoints"""
    print("Testing API endpoints...")
    
    try:
        # Test health endpoint
        response = requests.get("http://localhost:5000/health")
        if response.status_code != 200:
            print("✗ Health endpoint failed")
            return False
        
        # Test categories endpoint
        response = requests.get("http://localhost:5000/categories")
        if response.status_code != 200:
            print("✗ Categories endpoint failed")
            return False
        
        data = response.json()
        if "user_groups" not in data or "problem_categories" not in data:
            print("✗ Categories endpoint returned invalid data")
            return False
        
        print("✓ API endpoints working")
        return True
        
    except Exception as e:
        print(f"✗ Error testing API endpoints: {e}")
        return False

def main():
    """Run all tests"""
    print("AI Research Insights Platform - Setup Test")
    print("=" * 50)
    
    tests = [
        test_backend_dependencies,
        test_frontend_dependencies,
        test_environment_setup,
        test_backend_server,
        test_frontend_server,
        test_api_endpoints
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"✗ Test failed with error: {e}")
            results.append(False)
        print()
    
    print("=" * 50)
    print("Test Summary:")
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✓ All {total} tests passed! The platform is ready to use.")
        print("\nNext steps:")
        print("1. Open http://localhost:3000 in your browser")
        print("2. Try analyzing some research text")
        print("3. Test the accessibility features")
    else:
        print(f"✗ {total - passed} out of {total} tests failed.")
        print("\nPlease fix the issues above before using the platform.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)