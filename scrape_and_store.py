from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import csv
import os
import threading
import pandas as pd
from raksha import get_website_structure

filepath = "/home/tntra/Documents/verification/result.csv"
df = pd.read_csv(filepath)
companies = df["Company"].tolist()
urls = df['URL'].tolist()

# urls = ['https://www.tntra.io/', 'https://www.allegiant360.com/']
print(f"Total URLs to crawl: {len(urls)}")

for company,url in zip(companies,urls):
   get_website_structure(company, url)

print("All data scraped and stored in CSV files successfully.")
