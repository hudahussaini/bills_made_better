import requests
import json
import os

def main():
    # Base URL for the Congress.gov API
    BASE_URL = 'https://api.congress.gov/v3/bill'
    
    # Parameters
    API_KEY = os.getenv('CONGRESS_API_KEY')

    params = {
        'api_key': API_KEY,
        'format': 'json',
        'limit': 20,  # Number of results per page
        'sort': 'latestAction',
        'bill-status': 'passed-one',  # Bills that passed in one chamber
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            bills = data.get('bills', [])
            
            for bill in bills:
                print(f"Bill Number: {bill.get('number', 'N/A')}")
                print(f"Title: {bill.get('title', 'N/A')}")
                print(f"Latest Action Date: {bill.get('latestAction', {}).get('actionDate', 'N/A')}")
                print(f"Latest Action: {bill.get('latestAction', {}).get('text', 'N/A')}")
                print("-" * 50)
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print("Error message:", response.text)
            
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    main()