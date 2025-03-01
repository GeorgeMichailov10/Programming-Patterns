import requests
import json

BASE_URL = "http://127.0.0.1:5000/user"

def test_create_set():
    """Test creating a set of numbers."""
    response = requests.post(BASE_URL, json={"set": "2, 3, 4, 5"})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    assert "set" in data, "Response does not contain 'set'"
    assert data["set"] == [2, 3, 4, 5], f"Unexpected set: {data['set']}"
    return data["_id"]  # Return the ID for further testing

def test_get_set(set_id):
    """Test retrieving a specific set of numbers."""
    response = requests.get(BASE_URL, json={"id": set_id})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    assert "Set" in data, "Response does not contain 'Set'"
    assert data["Set"] == [2, 3, 4, 5], f"Unexpected set: {data['Set']}"

def test_add_number(set_id):
    """Test adding a number to an existing set."""
    response = requests.put(BASE_URL, json={"id": set_id, "add": 6})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    response = requests.get(BASE_URL, json={"id": set_id})
    assert response.status_code == 200
    data = response.json()
    assert data["Set"] == [2, 3, 4, 5, 6], f"Unexpected set after add: {data['Set']}"

def test_remove_number(set_id):
    """Test removing a number from an existing set."""
    response = requests.put(BASE_URL, json={"id": set_id, "remove": 6})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    
    # Verify the updated set
    response = requests.get(BASE_URL, json={"id": set_id})
    assert response.status_code == 200
    data = response.json()
    assert data["Set"] == [2, 3, 4, 5], f"Unexpected set after remove: {data['Set']}"

def test_calculation(set_id):
    """Test performing operations on a set."""
    response = requests.get(BASE_URL, json={"id": set_id, "operators": "+, -, *"})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    
    equation = "2 + 3 - 4 * 5"
    expected_result = ((2 + 3) - 4) * 5
    assert equation in data, "Equation format incorrect"
    assert data[equation] == expected_result, f"Unexpected calculation result: {data[equation]}"

def test_delete_set(set_id):
    """Test deleting a set."""
    response = requests.delete(BASE_URL, json={"id": set_id})
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    response = requests.get(BASE_URL, json={"id": set_id})
    assert response.status_code == 404, f"Set was not properly deleted, response: {response.json()}"

if __name__ == "__main__":
    set_id = test_create_set()
    test_get_set(set_id)
    test_add_number(set_id)
    test_remove_number(set_id)
    test_calculation(set_id)
    test_delete_set(set_id)
    print("All tests passed successfully!")
