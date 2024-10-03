import requests

# Базовый URL API
base_url = "https://petstore.swagger.io/v2"

# 1. GET-запрос для получения информации о питомце по ID
pet_id = 5
get_pet_url = f"{base_url}/pet/{pet_id}"
response_get_pet = requests.get(get_pet_url)

# Вывод статуса и текста ответа
print(f"GET {get_pet_url}")
print(f"Status code: {response_get_pet.status_code}")
print(f"Response: {response_get_pet.text}")

# 2. POST-запрос для добавления нового питомца
post_pet_url = f"{base_url}/pet"
new_pet_data = {
    "id": 999,
    "category": {"id": 0, "name": "string"},
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [{"id": 0, "name": "string"}],
    "status": "available"
}
response_post_pet = requests.post(post_pet_url, json=new_pet_data)

# Вывод статуса и текста ответа
print(f"POST {post_pet_url}")
print(f"Status code: {response_post_pet.status_code}")
print(f"Response: {response_post_pet.text}")

# 3. DELETE-запрос для удаления питомца по ID
delete_pet_url = f"{base_url}/pet/{pet_id}"
response_delete_pet = requests.delete(delete_pet_url)

# Вывод статуса и текста ответа
print(f"DELETE {delete_pet_url}")
print(f"Status code: {response_delete_pet.status_code}")
print(f"Response: {response_delete_pet.text}")
