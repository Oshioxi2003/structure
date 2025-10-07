"""
Test script to verify API endpoints
Run this after starting the server
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"


def test_user_endpoints():
    """Test user API endpoints"""
    print("=" * 50)
    print("Testing User API Endpoints")
    print("=" * 50)
    
    # Test 1: List users (should be empty or have admin)
    print("\n1. Testing GET /api/users/")
    response = requests.get(f"{BASE_URL}/users/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 2: Create a new user
    print("\n2. Testing POST /api/users/")
    new_user = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123",
        "first_name": "Test",
        "last_name": "User"
    }
    response = requests.post(f"{BASE_URL}/users/", json=new_user)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        user_data = response.json()
        print(f"Response: {json.dumps(user_data, indent=2)}")
        user_id = user_data.get('id')
        
        # Test 3: Get user detail
        print(f"\n3. Testing GET /api/users/{user_id}/")
        response = requests.get(f"{BASE_URL}/users/{user_id}/")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        # Test 4: Search users
        print("\n4. Testing GET /api/users/search/?q=test")
        response = requests.get(f"{BASE_URL}/users/search/?q=test")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    else:
        print(f"Error: {response.text}")
    
    print("\n" + "=" * 50)
    print("Test completed!")
    print("=" * 50)


if __name__ == "__main__":
    try:
        test_user_endpoints()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to server")
        print("Make sure the Django server is running:")
        print("  python manage.py runserver")
    except Exception as e:
        print(f"❌ Error: {e}")
