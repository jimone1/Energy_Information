import requests
API_KEY = ""
response = requests.get(f"https://api.eia.gov/category/?api_key={API_KEY}&category_id=3390106")
print(response.text)