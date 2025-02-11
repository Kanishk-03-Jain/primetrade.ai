# Cryptocurrency Market Analysis

## Overview
This project provides real-time market analysis of the top 50 cryptocurrencies based on market capitalization. The data is continuously updated using the **CoinGecko API** and stored in a **Google Sheets document** for live tracking. The analysis helps in monitoring price fluctuations, market dominance, and trading activities to make informed financial decisions.

## Features
- **Real-time Data Fetching**: Retrieves updated cryptocurrency data every 5 minutes.
- **Google Sheets Integration**: Automatically stores the latest market data in a live spreadsheet.
- **Comprehensive Analysis**: Includes price trends, market cap shifts, and asset performance insights.
- **Data Visualization**: Enables tracking of price changes, market dominance, and trading volumes.

## Data Collection
The project retrieves data using the **CoinGecko API** with the following key parameters:
- **vs_currency**: USD (prices are in US dollars)
- **order**: Sorted by market capitalization (market_cap_desc)
- **per_page**: 50 (retrieving top 50 cryptocurrencies)
- **price_change_percentage**: 24h (tracking percentage change in the last 24 hours)
- **locale**: English (default language)

### Stored Attributes
- **Name**: Full name of the cryptocurrency (e.g., Bitcoin, Ethereum).
- **Symbol**: Ticker symbol (e.g., BTC, ETH).
- **Current Price**: Latest market price in USD.
- **Market Capitalization**: Total market value (price × circulating supply).
- **Total Volume**: 24-hour trading volume.
- **Price Change (24h)**: Percentage change over the last 24 hours.
- **Fully Diluted Valuation**: Market cap if all tokens were in circulation.
- **High (24h)** / **Low (24h)**: Highest and lowest prices recorded in the past 24 hours.
- **Market Cap Change (24h)**: Percentage change in market cap over 24 hours.

## Google Sheets Integration
The project automatically updates a **Google Sheets document** with the latest data. This ensures live tracking and easy access to real-time cryptocurrency insights.

### Live Tracking
You can access the **live Google Sheets document** [here](https://docs.google.com/spreadsheets/d/1tSx4XlpqY7--TAsp83KhgeC54MN19qJc1DBFawBaK_I/edit?usp=sharing)

## Installation & Setup
### Prerequisites
- Python 3.10+
- Required libraries: `gspread`, `oauth2client`, `requests`, `pandas`
- A **Google Cloud** service account with Google Sheets API enabled

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Kanishk-03-Jain/primetrade.ai.git
   cd crypto-market-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure **Google Sheets API**:
   - Create a **Google Cloud** service account.
   - Enable **Google Sheets API**.
   - Download `credentials.json` and place it in the project folder.
   - Share the Google Sheet with the service account email.

4. Run the script:
   ```sh
   python main.py
   ```

## Usage
- The script fetches real-time cryptocurrency data every **5 minutes**.
- The data is stored and continuously updated in a **Google Sheet**.
- Users can analyze market trends, price movements, and trading volumes easily.

## Sample Output
Example of top 5 cryptocurrencies based on **market capitalization**:

| Rank | Name    | Symbol | Market Cap (USD)          |
|------|--------|--------|--------------------------|
| 1    | Bitcoin | BTC    | $1,904,653,633,329      |
| 2    | Ethereum | ETH  | $317,977,979,272        |
| 3    | Tether  | USDT  | $141,876,785,140        |
| 4    | XRP     | XRP   | $140,234,810,827        |
| 5    | Solana  | SOL   | $96,694,566,442         |

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the **MIT License**.

