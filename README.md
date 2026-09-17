# E-Commerce Product Data Extraction & Price Monitoring

A Python-based web scraping and price monitoring system that collects e-commerce product data, tracks previous prices, detects price changes, and generates structured Excel reports.

## 🚀 Features

- Extracts product titles and prices
- Extracts unique product IDs
- Scrapes multiple pages automatically
- Tracks previous product prices
- Detects price increases and decreases
- Generates price-change alerts
- Creates structured Excel reports
- Adds scraping timestamps
- Handles page-loading failures with retries
- Removes duplicate product IDs
- Automatically formats Excel columns
- Enables Excel filters and freezes the header row

## 🛠️ Tech Stack

- Python
- Playwright
- BeautifulSoup
- Pandas
- OpenPyXL
- Excel

## 🔄 Data Pipeline

Website  
↓  
Playwright  
↓  
BeautifulSoup  
↓  
Product Data Extraction  
↓  
Pandas DataFrame  
↓  
Previous Price Comparison  
↓  
Excel Report

## 📁 Project Structure

```text
ecommerce-price-monitor/
│
├── main.py
├── scraper.py
├── parser.py
├── requirements.txt
├── README.md
│
└── data/
    └── output/
⚙️ Installation

Clone the repository:

git clone https://github.com/MS-coder90/ecommerce-price-monitor.git

Move into the project directory:

cd ecommerce-price-monitor

Install dependencies:

pip install -r requirements.txt

Install Playwright browser:

playwright install
▶️ Run
python main.py

The program will:

Scrape four product pages
Extract product information
Compare current prices with previous prices
Detect price changes
Generate an Excel report

Generated reports are saved in:

data/output/
📊 Example Output

The system generates structured data containing:

Field	Description
title	Product name
price	Current product price
product_id	Unique product identifier
scraped_at	Scraping timestamp
price_previous	Previously recorded price
price_change	Difference between current and previous price
🧪 Testing

This project was tested using a public e-commerce demo website designed for web-scraping practice.

The current implementation successfully extracts 24 products across 4 pages and compares their current prices with previously stored prices.

🎯 Use Cases

This type of automation can be adapted for:

E-commerce price monitoring
Product data collection
Competitor price tracking
Market research
Inventory monitoring
Structured Excel reporting
Business data automation
🔮 Future Improvements
Email price-change notifications
Scheduled scraping
Database storage
Dashboard visualization
More product fields
Multi-website monitoring
Automated cloud deployment
👨‍💻 Author

Muhammad Saad

Python Automation & Web Scraping Developer

GitHub:
https://github.com/MS-coder90
