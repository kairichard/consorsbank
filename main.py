import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)

wait_in_secs = os.environ.get("WAIT", 2)

def get_amounts():
    driver.get("https://www.consorsbank.de/ev/-?$part=gallery.banking.accountmanagement.atomic.accountsoverview&docId=1339247")
    time.sleep(wait_in_secs)

    driver.find_element_by_id("username").send_keys(os.environ["username"])
    driver.find_element_by_id("passwort").send_keys(os.environ["password"])
    time.sleep(wait_in_secs)
    driver.find_element_by_id("passwort").send_keys(Keys.ENTER)
    time.sleep(wait_in_secs)
    return dict(total=driver.find_elements_by_css_selector("span.ev-amount ")[0].text.replace(".", "").replace(",", ".").replace(" EUR", ""))

def main():
    amounts = get_amounts()
    if "baseline" in os.environ:
        baseline = float(os.environ["baseline"]})
        amounts["change"] = "{0:.2f}".format((100 * float(amounts["total"])/baseline) - 100)
    print(json.dumps(amounts))

if __name__ == "__main__":
    main()


