from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup
import csv
import threading
import pandas as pd
from fpdf import FPDF
import os

# Define paths
csv_output_dir = "csv_files"
pdf_output_dir = "pdf_files_new"
os.makedirs(csv_output_dir, exist_ok=True)
os.makedirs(pdf_output_dir, exist_ok=True)

filepath = "/home/tntra/Documents/verification/result.csv"
df =  pd.read_csv(filepath)
urls = df['URL'].tolist()
# urls = ['https://www.tntra.io/']
print(len(urls))
print(f"Total URLs to crawl: {len(urls)}")

def generate_pdf_from_csv(csv_filepath, pdf_filepath):
    # Load CSV file
    data = pd.read_csv(csv_filepath)
    
    # Create a PDF document
    data['Text'] = data['Text'].fillna('')

    # Extract the Title and Text columns
    titles = data['Title']
    texts = data['Text']

    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to PDF
    for title, text in zip(titles, texts):
        pdf.set_font("Arial", style='B', size=14)  # Bold for title
        pdf.cell(0, 10, title.encode('latin1', 'replace').decode('latin1'), ln=True)
        pdf.set_font("Arial", size=12)  # Normal for text
        pdf.multi_cell(0, 10, text.encode('latin1', 'replace').decode('latin1'))
        pdf.ln(10)  # Add a line break between entries

    # Save the PDF
    pdf.output(pdf_filepath)
    print(f"PDF saved to {pdf_filepath}")

def is_same_domain(url, base_domain):
    parsed_extracted_url = urlparse(url)
    return parsed_extracted_url.netloc == base_domain

def is_unnecessary_url(url):
    unnecessary_patterns = ['login', 'signup', 'register', 'terms', 'privacy']
    return any(pattern in url for pattern in unnecessary_patterns)

def crawl(url,base_domain,csv_filepath):
    visited_urls = set()

    lock = threading.Lock()
    if url in visited_urls:
        return

    with lock:
        visited_urls.add(url)

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

        response = requests.get(url,headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all(['header', 'footer']):
            tag.decompose()

        title = soup.title.string if soup.title else 'No title'
        text = soup.get_text(separator=' ', strip=True)
        # print(f"Crawling URL: {url}")
        # print(f"Title: {title}")

        with open(csv_filepath, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([url, title, text])

        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

        threads = []
        for link in links:
            if is_same_domain(link, base_domain) and not is_unnecessary_url(link):
                thread = threading.Thread(target=crawl, args=(link,))
                threads.append(thread)
                thread.start()

        for thread in threads:
            thread.join()

    except requests.RequestException as e:
        print(f"Failed to crawl {url}: {e}")


for idx, url_to_scrape in enumerate(urls):
    parsed_url = urlparse(url_to_scrape)
    base_domain = parsed_url.netloc

    # Create CSV file for each URL
    csv_filename = f"website_{idx+1}.csv"
    csv_filepath = os.path.join(csv_output_dir, csv_filename)

    # Write headers to the CSV
    with open(csv_filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Title', 'Text'])

    # Crawl the URL and save the data in the CSV
    crawl(url_to_scrape, base_domain, csv_filepath)

    print(f"{idx+1}. Website URL: {url_to_scrape} scraped")
    # Generate PDF from the CSV
    pdf_filename = f"website_{idx+1}.pdf"
    pdf_filepath = os.path.join(pdf_output_dir, pdf_filename)
    generate_pdf_from_csv(csv_filepath, pdf_filepath)

print("All PDFs generated successfully.")
