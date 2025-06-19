import requests
import csv
import time
import re
from datetime import datetime

def extract_postcode(address):
    match = re.search(r'\b\d{5}\b', address)
    return match.group(0) if match else 'N/A'

def extract_city_state(address):
    parts = address.split(', ')
    if len(parts) > 2:
        city = parts[-3]  # Assuming city is the third last part
        state = parts[-2]  # Assuming state is the second last part
    else:
        city = 'N/A'
        state = 'N/A'
    return city, state

def get_places(keyword, location="Malaysia", radius=5000, api_key="[API KEY HERE]"):
    places = []
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}+in+{location}&radius={radius}&key={api_key}"
    
    while url:
        response = requests.get(url)
        data = response.json()
        
        if 'results' in data:
            for place in data['results']:
                name = place.get('name', 'N/A')
                address = place.get('formatted_address', 'N/A')
                postcode = extract_postcode(address)
                city, state = extract_city_state(address)
                place_id = place.get('place_id', '')
                
                # Get additional details like phone number and email (if available)
                details_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_phone_number,website&key={api_key}"
                details_response = requests.get(details_url)
                details_data = details_response.json()
                
                phone = details_data.get('result', {}).get('formatted_phone_number', 'N/A')
                website = details_data.get('result', {}).get('website', 'N/A')
                
                # Try to extract email from website (optional, but very rarely available this way)
                email = 'N/A'
                if website and "@" in website:
                    email = website
                
                places.append([name, phone, email, postcode, city, state, address])
        
        # Check for pagination token to get more results
        next_page_token = data.get('next_page_token')
        if next_page_token:
            time.sleep(2)  # Wait to avoid API rate limits
            url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"
        else:
            url = None
    
    return places

def save_to_csv(data, keyword, location):
    now = datetime.now().strftime("%Y-%m-%d %I.%M%p")
    keyword_clean = keyword.strip().capitalize()
    location_clean = location.strip().capitalize()
    filename = f"Google Maps {keyword_clean} {location_clean} {now}.csv"
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Postcode", "City", "State", "Address"])
        writer.writerows(data)
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    keyword = input("Enter the search keyword (e.g., cafe, hospital): ")
    location = input("Enter location (default: Malaysia): ") or "Malaysia"
    
    print(f"🔍 Searching for '{keyword}' in '{location}'...\nPlease wait...")
    results = get_places(keyword, location)
    save_to_csv(results, keyword, location)
    print("🎉 Done! Check the CSV file for results.")
