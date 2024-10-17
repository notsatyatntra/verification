from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from langchain_community.llms import Ollama
import time
import csv
# import docx

def phind_search(query):

    driver = webdriver.Chrome()
    # driver.minimize_window() 
    
    query_row = []
    sse = "Phind"
    query_row.append(sse)
    driver.get("https://www.phind.com/search?home=true")

    search_box = driver.find_element(By.TAG_NAME, "textarea")
    search_box.send_keys(query) 
    search_box.send_keys(Keys.ENTER)
    time.sleep(15)
    
    try:
        result_div = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "answer-0"))
        )
        final_result = ""
        results = result_div.find_elements(By.CSS_SELECTOR, 'div.fs-5')
        for result in results:
            final_result = final_result + result.text
        print(sse + ": Successfully found and stored results")
        return (final_result)
        
        
        # links = []
        # result_links = result_div.find_elements(By.TAG_NAME, "a")
        # for link in result_links:
        #     href = link.get_attribute("href")
        #     links.append(href)
        
        # query_row.append(final_result)
        # query_row.append(links)
        
        # with open("SSE_QueryResults.csv", "a+", newline="") as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow(query_row)
        

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()
        
    
def perplexity_search(query):

    driver = webdriver.Chrome()
    # driver.minimize_window()
    
       
    query_row = []
    sse = "Perplexity"
    query_row.append(sse)
    driver.get("https://www.perplexity.ai/")
    
    search_box = driver.find_element(By.TAG_NAME, "textarea")
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)
    time.sleep(15)
    
    try:
        result_div = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.break-words"))
        )
        # doc = docx.Document()
        # doc.add_paragraph(result_div.text)
        # doc.save("3_perplexity.docx")
        # print(result_div.text)
        if result_div.text == "None":
            perplexity_search(query)
        print(sse + ": Successfully found and stored results")

        return (result_div.text)
        
        # links = []
        # result_links = result_div.find_elements(By.TAG_NAME, "a")
        # for link in result_links:
        #     href = link.get_attribute("href")
        #     links.append(href)
        
        # query_row.append(result_div.text)
        # query_row.append(links)
        
        # with open("SSE_QueryResults.csv", "a+", newline="") as csvfile:
        #     csv_writer = csv.writer(csvfile)
        #     csv_writer.writerow(query_row)
        
        # print(sse + ": Successfully found and stored results")

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()        


def xdash_search(query):
    
    driver = webdriver.Chrome()
    # driver.minimize_window()
    
       
    # query_row = []
    sse = "Xdash"
    driver.get("https://www.xdash.ai/")

    search_box = driver.find_element(By.TAG_NAME, "input")
    search_box.send_keys(query)

    search_box.send_keys(Keys.ENTER)
    time.sleep(20)

    try:
        search_div = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "markdown-styles_reactMarkDown__Pl6_h"))
        )
        # search_results = search_div.find_elements(By.CSS_SELECTOR, 'div.fs-5')
        # final_result = ""
        # for result in search_results:
        #     final_result = final_result + result.text
        result = search_div.text
        print(sse + ": Successfully found and stored results")
        print(result)
        # search_links = search_div.find_elements(By.TAG_NAME, "a")
        # links = []
        # for link in search_links:
        #     href = link.get_attribute("href")
        #     links.append(href)
        
        # query_row.append(final_result)
        # query_row.append(links)
        return(result)

    except Exception as e:
        print("Error:", e)

    finally:
        driver.quit()  
    
            
def llama3_search(query):
    query_row = []
    query_row.append("Llama3")
    
    llm = Ollama(model='llama3')
    result = llm.invoke(query)
    print("Llama3 sccessfully found and stored results")
    return (result)
    
    # query_row.append(result)
    # with open("SSE_QueryResults.csv", "a+", newline="") as csvfile:
    #         csv_writer = csv.writer(csvfile)
    #         csv_writer.writerow(query_row)
            
        

def llama2_search(query):
    query_row = []
    query_row.append("Llama2")
    
    llm = Ollama(model='llama2')
    result = llm.invoke(query)
    print("Llama2 sccessfully found and stored results")

    return (result)
    
    # query_row.append(result)
    # with open("SSE_QueryResults.csv", "a+", newline="") as csvfile:
    #         csv_writer = csv.writer(csvfile)
    #         csv_writer.writerow(query_row)
    


def mistral_search(query):
    query_row = []
    query_row.append("Mistral")
    
    llm = Ollama(model='mistral')
    result = llm.invoke(query)
    print("Mistral sccessfully found and stored results")
    return (result)
    
    # query_row.append(result)
    # with open("SSE_QueryResults.csv", "a+", newline="") as csvfile:
    #         csv_writer = csv.writer(csvfile)
    #         csv_writer.writerow(query_row)


# queries = [
#     "Give me a list of companies that provide Electric Vehicle (EV) charging facilities in the UAE.",
#     "Give me a list of EV brands selling in the UAE.",
#     "Give me information about the EV selling trends in the UAE over the last 2 years.",
#     "Give me the percentage sales of Tesla in the UAE. Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Audi in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of BMW in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Porsche in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Mercedes-Benz in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of HiPhi in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of BYD in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Barq EV in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Ceer in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of MENA Mobility in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me the percentage sales of Mays Motors in the UAE.  Give the answer in the format: Company_Name -percentage sales. Do not give any other text information.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Dubai Electricity and Water Authority (DEWA) in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Etihad Water and Electricity in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by GreenParking in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by ChargeMap in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Al Futtaim Automotive Group in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Regeny & EvGateway in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Sharjah Electricity and Water Authority (SEWA) in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Abu Dhabi Distribution Company (ADDC) in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by Tesla Superchargers in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me a list of accompanying facilities at EV charging stations operated by ABB Group in the UAE. Do not give any introduction or outro or any extra information. Just provide a list format of facilities provided by each company under their name.",
#     "Give me EV charging costs for Dubai Electricity and Water Authority (DEWA) in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Etihad Water and Electricity in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for GreenParking in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for ChargeMap in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Al Futtaim Automotive Group in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Regeny & EvGateway in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Sharjah Electricity and Water Authority (SEWA) in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Abu Dhabi Distribution Company (ADDC) in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for Tesla Superchargers in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me EV charging costs for ABB Group in UAE over the last 2 years. Give me the answer in the format of 10A:10A-charging cost, 16A:16A-charging cost, 32A:32A-charging cost with the respective year. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Dubai Electricity and Water Authority (DEWA) in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Etihad Water and Electricity in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by GreenParking in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by ChargeMap in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Al Futtaim Automotive Group in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Regeny & EvGateway in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Sharjah Electricity and Water Authority (SEWA) in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Abu Dhabi Distribution Company (ADDC) in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by Tesla Superchargers in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Give me customer reviews of EV charging stations operated by ABB Group in the UAE. Only give me the average star rating. Do not give any other text information.",
#     "Tell me if Dubai Electricity and Water Authority (DEWA) is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Etihad Water and Electricity is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if GreenParking is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if ChargeMap is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Al Futtaim Automotive Group is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Regeny & EvGateway is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Sharjah Electricity and Water Authority (SEWA) is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Abu Dhabi Distribution Company (ADDC) is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if Tesla Superchargers is listed. Answer in just 'Yes' or 'No' format only.",
#     "Tell me if ABB Group is listed. Answer in just 'Yes' or 'No' format only.",
#     "Give me a list of products or services offered by Dubai Electricity and Water Authority (DEWA) globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Etihad Water and Electricity globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by GreenParking globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by ChargeMap globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Al Futtaim Automotive Group globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Regeny & EvGateway globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Sharjah Electricity and Water Authority (SEWA) globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Abu Dhabi Distribution Company (ADDC) globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Tesla Superchargers globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by ABB Group globally. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Dubai Electricity and Water Authority (DEWA) in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Etihad Water and Electricity in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by GreenParking in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by ChargeMap in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Al Futtaim Automotive Group in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Regeny & EvGateway in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Sharjah Electricity and Water Authority (SEWA) in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Abu Dhabi Distribution Company (ADDC) in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by Tesla Superchargers in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "Give me a list of products or services offered by ABB Group in the UAE. Do not give any introduction or outro or any extra information.Just provide a list format of products and services and a brief description of each.",
#     "How many patents filed by DEWA in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by Etihad Water and Electricity in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by GreenParking in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by ChargeMap in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by Al Futtaim Automotive Group in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by Regeny & EvGateway in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by SEWA in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information ",
#     "How many patents filed by ADDC in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by Tesla Superchargers in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents filed by ABB Group in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by Dubai Electricity and Water Authority (DEWA) in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by Etihad Water and Electricity in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by GreenParking in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by ChargeMap in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by Al Futtaim Automotive Group in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by Regeny & EvGateway in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by SEWA in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by ADDC in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by Tesla Superchargers in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "How many patents obtained by ABB Group in the last 7 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "Give me the monthly stock price variation for Dubai Electricity and Water Authority (DEWA) operating in the UAE over the last 3 years. Give the data in the format of year: patents-filed. Do not give any other text information",
#     "Give me the monthly stock price variation for Etihad Water and Electricity operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for GreenParking operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for ChargeMap operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for Al Futtaim Automotive Group operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for Regeny & EvGateway operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for Sharjah Electricity and Water Authority (SEWA) operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for Abu Dhabi Distribution Company (ADDC) operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for Tesla Superchargers operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
#     "Give me the monthly stock price variation for ABB Group operating in the UAE over the last 3 years. Give me data in the format of : month:stock_price. Do not give any other text information.",
# ]

# queries = [
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by JMS Inc in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Meiji Seika Kaisha Ltd in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Kumiai Chemical Industry Co., Ltd. in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Nippon Kayaku Co., Ltd. in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Tosoh Corporation in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Kureha Corporation in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Showa Denko K.K. in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Toyobo Co., Ltd. in Japan.",
#  "You are an expert market researcher and business analyst.You can also act as a domain expert. I want to start a business and that is why I am consulting you. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted) .Just provide a list format of facilities provided by each company under their name.Here is the question: Give me a list of accompanying facilities for Biofertilizers provided by Shin-Etsu Chemical Industries, Ltd.' in Japan.",

# ]
service_name = 'Road Transport'
country_name = 'UAE'

queries = [f"""You are an expert market researcher and business analyst. You can also act as a domain expert.  I want to start/grow a business and that is why I am consulting you on their behalf. Your goal is to deliver actionable intelligence that informs business decisions and drives growth within the targeted market. Provide me proper statistical information for the numeric questions and in depth answers for the theoretical data.Do not give any introduction or outro or any extra information. Just specify at last if your given output is based on real data then state (Based on real data) and if you have made predictions then state (Predicted), Give it only in a format of python list : example - ["Company1","Company2","Company3"]. Cross verify and name only the companies that actually exists and deal with this. Which are the top companies that provide {service_name} in {country_name}?"""]

for query in queries:
    result = []
    result.append(query)
    
    # data = xdash_search(query)
    # result.append(data)
    # print(data)
    
    data = perplexity_search(query)
    result.append(data)
    print(data)
    
    data = llama3_search(query)
    result.append(data)
    print(data)
    
    data = llama2_search(query)
    result.append(data)
    print(data)
    
    data = mistral_search(query)
    result.append(data)
    print(data)
    
    with open("GLS_facility_results.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(result)
