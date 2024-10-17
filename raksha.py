import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import csv
import os



class WebScrapeConstant:
   IMG_EXTENSION = [".png", ".jpg", ".jpeg", ".gif", ".svg"]


# Define paths
csv_output_dir = "csv_files"
os.makedirs(csv_output_dir, exist_ok=True)

def get_website_structure(website_name, website_url):
   headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
   }


   def get_title_and_content(url):
       try:
           response = requests.get(url, headers=headers, timeout=10)
           response.raise_for_status()
           soup = BeautifulSoup(response.text, "html.parser")
           title = soup.title.text.strip() if soup.title else "No Title"
           content = " ".join(soup.stripped_strings)
        #    pdf_urls = get_pdf_urls(soup, url)
        #    image_urls = get_image_urls(soup, url)
           return title, content
    #    , pdf_urls, image_urls
       except Exception as e:
           print(f"Error fetching {url}: {e}")
           return "Error", "", [], []


#    def get_pdf_urls(soup, website):
#        """Function to extract PDF URLs from a given website."""
#        pdf_links = soup.find_all(
#            "a",
#            href=lambda href: href
#            and (href.lower().endswith(".pdf") or ".pdf?" in href.lower()),
#        )
#        pdf_list = set(urljoin(website, link["href"]) for link in pdf_links)
#        return list(pdf_list)


#    def get_image_urls(soup, website):
#        """Function to extract image URLs from a given website."""
#        image_links = soup.find_all(
#            "img",
#            src=lambda src: src
#            and any(
#                src.lower().endswith(ext) for ext in WebScrapeConstant.IMG_EXTENSION
#            ),
#        )
#        image_list = set(urljoin(website, img["src"]) for img in image_links)
#        return list(image_list)


   try:
       response = requests.get(website_url, headers=headers, timeout=10)
       response.raise_for_status()
       soup = BeautifulSoup(response.text, "html.parser")
       nav_items = soup.find_all("a", href=True)
   except Exception as e:
       print(f"Error fetching {website_url}: {e}")
       return


   categories = {}
   exclude_keywords = [
       "privacy",
       "terms",
       "conditions",
       "wp-content",
       ".png",
       ".jpg",
       ".jpeg",
   ]


   for item in nav_items:
       href = item["href"]
       if href.startswith("#") or href.startswith("javascript:"):
           continue


       full_url = urljoin(website_url, href)
       parsed_url = urlparse(full_url)


       if (
           parsed_url.scheme in ["http", "https"]
           and parsed_url.netloc == urlparse(website_url).netloc
       ):
           path = parsed_url.path.strip("/")
           if not path:
               continue


           path_parts = path.split("/")
           category = path_parts[0] if path_parts else "Other"


           if any(keyword in href.lower() for keyword in exclude_keywords):
               continue


           if category not in categories:
               categories[category] = {"urls": set(), "subcategories": {}}


           subcategory = path_parts[1] if len(path_parts) > 1 else None


           if subcategory:
               if subcategory not in categories[category]["subcategories"]:
                   categories[category]["subcategories"][subcategory] = set()
               categories[category]["subcategories"][subcategory].add(full_url)
           else:
               categories[category]["urls"].add(full_url)


   csv_filename = f"{website_name.replace(' ', '_')}_structure.csv"
   csv_filepath = os.path.join(csv_output_dir, csv_filename)

   with open(csv_filepath, mode="w", newline="", encoding="utf-8") as file:
       writer = csv.writer(file)
       writer.writerow(["Name", "URL", "Content", "PDF URLs", "Image URLs"])


       main_title, main_content = get_title_and_content(website_url)
       writer.writerow(
           [
               website_name,
               website_url,
               main_content,
            #    "; ".join(main_pdfs),
            #    "; ".join(main_images),
           ]
       )


       for category, data in categories.items():
           category_url = list(data["urls"])[0] if data["urls"] else website_url
           category_title, category_content = (
               get_title_and_content(category_url)
           )
           writer.writerow(
               [
                   category,
                   category_url,
                   category_content,
                #    "; ".join(category_pdfs),
                #    "; ".join(category_images),
               ]
           )


           for subcategory, urls in data["subcategories"].items():
               subcategory_url = list(urls)[0]
               (
                   subcategory_title,
                   subcategory_content,
                #    subcategory_pdfs,
                #    subcategory_images,
               ) = get_title_and_content(subcategory_url)
               writer.writerow(
                   [
                       subcategory,
                       subcategory_url,
                       subcategory_content,
                #        "; ".join(subcategory_pdfs),
                #        "; ".join(subcategory_images),
                   ]
               )


               for url in urls:
                   if url != subcategory_url:
                       title, content = get_title_and_content(url)
                       writer.writerow(
                           [title, url, content]
                       )


        #    for url in data["urls"]:
            #    if url != category_url:
            #        title, content, pdfs, images = get_title_and_content(url)
            #        writer.writerow(
            #            [title, url, content, "; ".join(pdfs), "; ".join(images)]
            #        )


   print(f"Data for {website_name} has been saved to {csv_filename}")




# List of websites
# lists = [
#    {"name": "Tntra", "url": 'https://www.tntra.io/'},
# ]


# for website in lists:
#    get_website_structure(website["name"], website["url"])
