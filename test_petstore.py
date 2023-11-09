import requests

base_url = "https://petstore.swagger.io/v2"

# ***** Endpoint 1:pet by ID *****
pet_id = int(input("Enter ID : "))
pet_by_id_url = f"{base_url}/pet/{pet_id}"

response_pet_by_id = requests.get(pet_by_id_url)
print(f"Response from {pet_by_id_url}: {response_pet_by_id.json()}")

# ***** Endpoint 2:pets by status *****
status = "available"
pets_by_status_url = f"{base_url}/pet/findByStatus?status={status}"

response_find_pets_by_status = requests.get(pets_by_status_url)
print(f"Response from {pets_by_status_url}: {response_find_pets_by_status.json()}")


# ***** Endpoint 3:inventory status *****
inventory_url = f"{base_url}/store/inventory"

response_inventory = requests.get(inventory_url)
print(f"Response from {inventory_url}: {response_inventory.json()}")
