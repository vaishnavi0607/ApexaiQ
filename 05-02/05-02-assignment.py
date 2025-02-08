"""Scrapping Windows 11 release information"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

class Scrapper:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=self.options)
        time.sleep(2)
        self.driver.get("https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information")
        elements = self.driver.find_elements(By.XPATH,'//*[@id="winrelinfo_container"]/details/summary/strong')

        for element in elements:
            element.click()

    def extract(self):
        tables_data = []
        
        for all_tables in self.driver.find_elements(By.XPATH, "//table"):
            heading = []
            data = []
            
            # Extract headers
            header_row = all_tables.find_elements(By.XPATH, ".//tr")[0]
            for th in header_row.find_elements(By.XPATH, ".//th"):
                heading.append(th.text)
            
            # Extract data rows
            for tr in all_tables.find_elements(By.XPATH, ".//tr")[1:]:
                row = []
                for td in tr.find_elements(By.XPATH, ".//td"):
                    row.append(td.text)
                if row:  
                    data.append(row)
            
            if heading and data:  
                tables_data.append((heading, data))
        
        # Save all tables to the same CSV file
        with open("combined_table.csv", "w", newline='', encoding='utf-8') as file:
            for i, table in enumerate(tables_data):
                headers = table[0]  
                rows = table[1]  
                df = pd.DataFrame(rows, columns=headers)
                
                # Write headers for the first two tables
                if i < 2:
                    df.to_csv(file, index=False)
                else:
                    # Write headers only once for the remaining tables
                    if i == 2:
                        df.to_csv(file, index=False)
                    else:
                        df.to_csv(file, index=False, header=False)
                
                print(df)
                print("\n")  

scrapper = Scrapper()
scrapper.extract()