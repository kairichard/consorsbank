import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

wait_in_secs = os.environ.get("WAIT", 3)

def login():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.consorsbank.de/ev/-?$part=gallery.banking.accountmanagement.atomic.accountsoverview&docId=1339247")
    time.sleep(wait_in_secs)

    driver.find_element_by_id("user-id").send_keys(os.environ["username"])
    driver.find_element_by_id("password").send_keys(os.environ["password"])
    time.sleep(wait_in_secs)
    driver.find_element_by_id("login").click()
    time.sleep(wait_in_secs)
    return driver

def get_total():
    driver = login()
    time.sleep(wait_in_secs)
    return dict(total=driver.find_elements_by_css_selector("span.ev-amount ")[0].text.replace(".", "").replace(",", ".").replace(" EUR", ""))

def get_total_by_account(account):
    driver = login()
    driver.get("https://www.consorsbank.de/ev/Mein-Konto-und-Depot/Konten/Umsaetze-und-Zahlungsverkehr/Umsaetze?accountNo="+account)
    time.sleep(wait_in_secs)
    driver.get("https://www.consorsbank.de/ev/rest/de/user/accounts/selectedaccount/dataselectedaccount")
    time.sleep(wait_in_secs)
    return json.loads(driver.find_elements_by_css_selector("pre")[0].text)["selectedAccount"]["accountBalance"]

def get_categories():
    driver = login()
    driver.get("https://www.consorsbank.de/ev/rest/de/user/accounts/pfm/categories")
    return driver.find_elements_by_css_selector("pre")[0].text

def main():
    what = sys.argv[1]
    if what == "total":
        amounts = get_total()
        print(json.dumps(amounts))
    elif what == "categories":
        print(get_categories())
    elif what == "account":
        print(get_total_by_account(sys.argv[2]))
    else:
        print("Unkown argument")

if __name__ == "__main__":
    main()


