# 🗺️ Google Maps Business Scraper  

A Python script that scrapes business listings from Google Maps based on user input (business type + location) and exports the data to an Excel file.  

⚠️ **Note**: Due to Google's limitations, this tool fetches up to **60 results per query**. Requires a **Google Geolocation API key**.  

---

## 🚀 Features  
- **Input**: Specify a business type (e.g., "coffee shops") and location (e.g., "New York").  
- **Output**: Generates an Excel file (`businesses.xlsx`) with:  
  - Business names  
  - Addresses  
  - Contact details (phone, website)  
  - Ratings and reviews  
- **Automated**: Uses Selenium to interact with Google Maps.  

---

## ⚙️ Setup  

### Prerequisites  
1. **Python 3.x** ([Download here](https://www.python.org/downloads/))  
2. **Google Maps API Key** ([Get one here](https://developers.google.com/maps/documentation/geolocation/get-api-key))  
3. **Chrome Browser** (or update the script to use another browser)  

### Installation  
1. Clone this repository or download the script:  
   ```bash
   git clone https://github.com/yourusername/google-maps-scraper.git
   cd google-maps-scraper
