import requests
import random

def search_store_on_yelp(location):
    API_Key = "xgzrxqPH6jTbrs4NWK7WANs1SrFJKtPg57m5L2aSpQAV0mWH839-VUjxq1psmTpi_2D3mDDC2Qi-VXbt2jenLa8MaGmsMOjyruOXvygjRhdicYKwIR3JgemMZZh9Z3Yx"
    headers = {"Authorization": f"Bearer {API_Key}"}
    url = "https://api.yelp.com/v3/businesses/search"

    random_offset = random.randint(0, 50)

    # api request parameters
    params = {
        "term": "boba",
        "location": location,
        "categories": "bubble tea",
        "limit": 12,
        "offset": random_offset
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('businesses', [])
    else:
        print(f"Error: {response.status_code} - Unable to retrieve data. Please check your network connection and try again")
        return []


def boba_picker():
    print("Welcome to the Automatic Boba Picker!")
    location = input("Enter your city or zip code: ").strip()

    # use Yelp api to find boba stores
    boba_stores = search_store_on_yelp(location)

    if not boba_stores:
        print("\nNo boba stores found. Please try again.")
        return

    print(f"\nFound {len(boba_stores)} boba stores in {location}.\n")

    filtered_stores = []
    for store in boba_stores:
        print(f"Found boba store being added to list: {store['name']}")

    print("\nRandomly choosing a store from the list now...")

    random_choice = random.choice(boba_stores)
    print(f"\n🎉 You should try {random_choice['name']}!")
    print(f"📍 Address: {', '.join(random_choice['location']['display_address'])} | ⭐️ Rating: {random_choice['rating']}\n")


# run program
if __name__ == "__main__":
    boba_picker()
