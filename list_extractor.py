# Extract list of companies from the LLM output

import re

texts = ["""["Arabian Logistics", "DP World", "Etihad Rail DB Schenker", "Emirates Logistics Company (ELC)", "Maersk Line"] (Based on real data)""",
         """["Aramex Logistics", "DHL Global Forwarding", "FedEx Middle East, Indian Subcontinent & Africa", "UPS Middle East and Africa", "Agility Logistics"] Based on real data, these are the top road transport companies operating in the UAE. Each of these companies offers a comprehensive range of logistics solutions, including road transportation, across various industries. Their strong market presence is built upon their reliable services, efficient operations, and wide geographical coverage. By partnering with any of these established players, your business can benefit from their expertise, resources, and extensive network to successfully navigate the competitive landscape of road transport in UAE.""",
        #  """Based on real data, the top companies that provide road transportation services in UAE are:[["Abu Dhabi National Trucking Company (ADNTC)","Al Futaim Logistics","Aramex International"]]Please note that this list is based on a general search of reputable sources and may not be exhaustive or up-to-date. Its always best to cross-check and verify information from multiple sources before making any business decisions.""",
         """["BBC International Transport and Logistics Services Company", "Al Mas Cargo LLC", "Haulier", "Freezchill", "Creek General Transport", "Total Freight International", "Aramex", "Global Shipping and Logistics LLC"] (Based on real data)"""]

final_company_list = []
for text in texts:
    # Use regular expression to find the list
    pattern = r'\[.*\]'
    match = re.search(pattern, text)

    if match:
        extracted_list = eval(match.group())
        print(extracted_list)
        final_company_list.extend(extracted_list)
    else:
        print("No list found in the text.")

final_company_list = list(set(final_company_list))     
print(final_company_list)
