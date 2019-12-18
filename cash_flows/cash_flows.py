# Imports
import os
from platform import system
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re


def get_report(ticker):

    # Set up headless Chrome on Selenium
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    # Look in this filepath
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Check operating system
    if system() == "Windows":
        CHROME_PATH = r"../chromedriver_windows.exe"
    elif system() == "Darwin":
        CHROME_PATH = r"../chromedriver_mac"
    elif system() == "Linux":
        CHROME_PATH = r"../chromedriver_linux"

    driver = webdriver.Chrome(CHROME_PATH, options=options)

    # Load company search page
    driver.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=10-k&dateb=&owner=exclude&count=10".format(ticker))

    # Navigate to 10-K
    document = driver.find_element_by_link_text("Interactive Data")
    document.click()
    sleep(3)

    # Load financial statements
    menu = driver.find_element_by_link_text("Financial Statements")
    menu.click()
    sleep(2)

    # Load Consolidated Statements of Cash Flows
    try:
        cash_flows = driver.find_element_by_partial_link_text("Cash Flows")

    except:
        cash_flows = driver.find_element_by_partial_link_text("CASH FLOWS")

    cash_flows.click()

    # Identify table data
    table = driver.find_element_by_class_name("report")

    # Get report
    return table.get_attribute("innerHTML")

print(get_report("aapl"))
