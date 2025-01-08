import requests
import random

def search_store_on_yelp(location):
    API_Key = "xgzrxqPH6jTbrs4NWK7WANs1SrFJKtPg57m5L2aSpQAV0mWH839-VUjxq1psmTpi_2D3mDDC2Qi-VXbt2jenLa8MaGmsMOjyruOXvygjRhdicYKwIR3JgemMZZh9Z3Yx"
    headers = {"Authorization": f"Bearer {API_Key}"}
    url = "https://api.yelp.com/v3/businesses/search"

    # api request parameters
    params = {
        "term": "boba",
        "location": location,
        "categories": "boba",
        "limit": 5
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('businesses', [])
    else:
        print(f"Error: {response.status_code} - Unable to retrieve data. Please check your network connection and try again")
        return []

def get_reviews(business_id):
    API_Key = "xgzrxqPH6jTbrs4NWK7WANs1SrFJKtPg57m5L2aSpQAV0mWH839-VUjxq1psmTpi_2D3mDDC2Qi-VXbt2jenLa8MaGmsMOjyruOXvygjRhdicYKwIR3JgemMZZh9Z3Yx"
    headers = {"Authorization": f"Bearer {API_Key}"}
    url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reviews = [review['text'].lower() for review in data['reviews']]
        return reviews
    else:
        print(f"Error: Unable to retrieve reviews for business ID: {business_id}")
        return []

def boba_picker():
    print("Welcome to the Automatic Deicision Maker: Boba Store Edition!")
    location = input("Enter your city: ").strip()

    # use Yelp api to find boba stores
    boba_stores = search_store_on_yelp(location)

    if not boba_stores:
        print("\nNo boba stores found. Please try again.")
        return

    print(f"Found {len(boba_stores)} boba stores in {location}.")

    # ask user if they are craving a specific drink
    craving = input("\nAre you craving a specific drink (e.g., matcha, green milk tea, taro)? If not, press 'Enter' to skip: ").lower().strip()

    if craving: # if the user is craving something specific
        filtered_stores = []
        for store in boba_stores:
            print(f"Fetching reviews for: {store['name']}, Business ID: {store['id']}")
            # get reviews for the store using reviews api which has more specific drink names
            reviews = get_reviews(store['id'])  # retrieve top 3 reviews
            if any(craving in review for review in reviews):
                filtered_stores.append(store)
                print(f"'{craving}' found in reviews for: {store['name']}!")

        if filtered_stores: # if the stores match the craving
            chosen_store = random.choice(filtered_stores)
            print(f"\nYou should go to {chosen_store['name']} for your craving!")
        else:   # if no store matches the craving
            print(f"\nSorry, no boba store mentions '{craving}'. Let's pick from the list.")
            random_choice = random.choice(boba_stores)  
            print(f"\nYou should try {random_choice['name']}!")
    else:   # if the user has no cravings
        chosen_store = random.choice(boba_stores)
        print(f"\nYou should go to {chosen_store['name']}!")


# run program
if __name__ == "__main__":
    boba_picker()