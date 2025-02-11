import requests
import pandas as pd
import time
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets authentication setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Crypto Live Data").sheet1


API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
}

# Assignment step 1- Fetch Live Data
def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data", response.status_code)
        return []

def process_data(data):
    df = pd.DataFrame(data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h", "fully_diluted_valuation", "high_24h", "low_24h", "market_cap_change_percentage_24h"])
    return df

# Assignment step 2- Data Analysis
def analyze_data(df):
    top_5 = df.nlargest(5, "market_cap")[["name", "market_cap"]]
    avg_price = df["current_price"].mean()
    highest_change = df.loc[df["price_change_percentage_24h"].idxmax(), ["name", "price_change_percentage_24h"]]
    lowest_change = df.loc[df["price_change_percentage_24h"].idxmin(), ["name", "price_change_percentage_24h"]]
    
    return top_5, avg_price, highest_change, lowest_change


# Assignment step-3 - Live-Running Excel Sheet
def update_excel(df, filename="crypto_data.xlsx"):
    try:
        wb = Workbook()
        ws = wb.active
        ws.title = "Live Crypto Data"
        
        ws.append(df.columns.tolist())  # Adding column names in excel
        
        for row in dataframe_to_rows(df, index=False, header=False):
            ws.append(row)
        
        wb.save(filename)
        print(f"Updated {filename} with latest data.")
    except Exception as e:
        print("Error updating Excel:", e)

def update_google_sheets(df):
    # Access sheet at https://docs.google.com/spreadsheets/d/1tSx4XlpqY7--TAsp83KhgeC54MN19qJc1DBFawBaK_I/edit?usp=sharing
    sheet.clear()
    sheet.insert_row(df.columns.tolist(), 1)
    sheet.insert_rows(df.values.tolist(), 2)
    print("Google Sheet updated successfully.")

def main():
    while True:
        print("Fetching latest cryptocurrency data...")
        data = fetch_crypto_data()
        if data:
            df = process_data(data)
            update_excel(df)
            update_google_sheets(df)
            top_5, avg_price, highest_change, lowest_change = analyze_data(df)
            print("Top 5 Cryptocurrencies by Market Cap:")
            print(top_5)
            print(f"\nAverage Price of Top 50: ${avg_price:.2f}")
            print(f"\nHighest 24h Change: {highest_change['name']} ({highest_change['price_change_percentage_24h']:.2f}%)")
            print(f"Lowest 24h Change: {lowest_change['name']} ({lowest_change['price_change_percentage_24h']:.2f}%)\n")
        
        print("Waiting for next update...")
        time.sleep(300)  # Update every 5 minutes

main()
