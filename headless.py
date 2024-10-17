# Code to store company URL from company names list

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from list_extractor import final_company_list


# Initialize Chrome driver
driver = webdriver.Chrome()

def headless(company_name):
    time.sleep(1)

    driver.get("https://www.google.com/")

    search_input = driver.find_element(By.TAG_NAME, "textarea")

    search_query = f"{company_name} UAE road transportation"
    search_input.send_keys(search_query)
    time.sleep(1)

    # Trigger the search
    search_input.send_keys(Keys.ENTER)

    # Wait for the search results to load
    time.sleep(1)

    # close_element = driver.find_element(By.CSS_SELECTOR, "button.contextual-sign-in-modal__modal-dismiss")
    # close_element.click()
    try:
        location_element = driver.find_element(By.CLASS_NAME, "yuRUbf")
        location_element.click()
        time.sleep(2)  # Wait for the new page to load
            
        # Extract the URL of the current page
        current_url = driver.current_url
        return current_url
    except:
        return 'Not Found'
    
    # try:
    #     close_element = driver.find_element(By.CSS_SELECTOR, "button.contextual-sign-in-modal__modal-dismiss")
    #     close_element.click()
    # except:
    #     pass
    # time.sleep(1)  # Wait for the page to load
    # try:
    #     location_element = driver.find_element(By.CLASS_NAME, "top-card-layout__first-subline")
    # except:
    #     try:
    #         location_element = driver.find_element(By.CLASS_NAME, "not-first-middot")
    #     except:    
    #         try:
    #             location_element = driver.find_element(By.CLASS_NAME, "top-card-layout__first-subline font-sans text-md leading-open text-color-text-low-emphasis")
    #         except:
    #             return 'Not Found'

    # return location_element.text

csv_file = 'result.csv'
header = ['Company', 'URL']

# Check if the CSV file already exists and write the header if it doesn't
try:
    with open(csv_file, 'x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
except FileExistsError:
    pass

for company_name in final_company_list:
    res = headless(company_name)
    # res = res.split(",")
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([company_name, res])
    print([company_name, res])


driver.quit()
