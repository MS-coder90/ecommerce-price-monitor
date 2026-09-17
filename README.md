# E-Commerce Product Data Extraction & Price Monitoring

A Python-based automation project that extracts e-commerce product data, tracks previous prices, detects price changes, and generates a formatted Excel report.

## Features

- Product data extraction
- Product title and price parsing
- Previous price tracking
- Automatic price change detection
- Price increase/decrease alerts
- Excel report generation
- Automatic Excel formatting
- Error handling for failed page requests
- Timestamped data collection

## Tech Stack

- Python
- Playwright
- BeautifulSoup
- Pandas
- OpenPyXL
- Excel

## Data Flow

Website
→ Playwright
→ BeautifulSoup
→ Data Extraction
→ Pandas
→ Price Comparison
→ Excel Report

## Project Structure

```text
ecommerce-price-monitor/
│
├── main.py
├── scraper.py
├── parser.py
├── requirements.txt
└── README.md

Installation

Install the required Python packages:

pip install -r requirements.txt

Install Playwright browser:

playwright install
Run the Project
python main.py

The project extracts product information and generates an Excel report containing:

Product title
Current price
Previous price
Price change
Scraped timestamp
Testing

The project was tested using a public e-commerce demo website designed for scraping practice.

The implementation demonstrates the complete workflow of product data extraction, price monitoring, comparison, and Excel reporting.

Future Improvements
Support for additional product sources
More advanced price tracking
Scheduled execution
Database storage
Email notifications
Dashboard integration
Author

Muhammad Saad
