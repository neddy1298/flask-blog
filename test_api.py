import requests
import json

BASE_URL = 'http://localhost:5001'

def test_registration():
    url = f"{BASE_URL}/api/user"
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "test123",
        "image_file": "default.jpg"
    }
    response = requests.post(url, json=data)
    print("Registration Response:", response.status_code)
    print(response.json() if response.status_code == 200 else response.text)

def test_get_users():
    url = f"{BASE_URL}/api/user/all"
    response = requests.get(url)
    print("\nGet Users Response:", response.status_code)
    print(response.json() if response.status_code == 200 else response.text)

def test_create_post():
    url = f"{BASE_URL}/api/post"
    data = {
        "title": "Test Post",
        "content": "This is a test post content",
        "user_id": 1
    }
    response = requests.post(url, json=data)
    print("\nCreate Post Response:", response.status_code)
    print(response.json() if response.status_code == 200 else response.text)

def test_get_posts():
    url = f"{BASE_URL}/api/post/all"
    response = requests.get(url)
    print("\nGet Posts Response:", response.status_code)
    print(response.json() if response.status_code == 200 else response.text)

if __name__ == "__main__":
    print("Testing API endpoints...")
    test_registration()
    test_get_users()
    test_create_post()
    test_get_posts()
