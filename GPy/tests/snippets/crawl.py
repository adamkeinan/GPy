# Import Libraries
import requests
from selenium import webdriver
from lxml import html
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
from selenium.webdriver.chrome.options import Options


def crawl_website(product, xpath_dict):
    # Set up parameters
    base_url = "https://www.website.com/product/{sku}/sellers"


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
}

product = product
product_name = product.title
map_price = product.map_price
asin = product.asin
sku = product.sku

# Retrieve Webpage
full_url = base_url.format(sku=sku)
time_stamp = pytz.utc.localize(datetime.utcnow())
page = requests.get(full_url, headers=headers)
doc = html.fromstring(page.content)

# Extract Price Field
original_price = doc.xpath(xpath_dict["original_price"])

# Discount
discount = [
    str(100 * max(0.0, round(1 - float(i) / float(map_price), 2))) + "%"
    for i in original_price
]

# MAP Violation Field
map_violation = [float(i) < float(map_price) for i in original_price]

# Extract Seller Names
seller_name = doc.xpath(xpath_dict["seller_name"])

# If a violation is found, take a screenshot
screenshot = None
if True in map_violation:
    # Screenshot of Current URL
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    DRIVER = "chromedriver"
    driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)
    driver.get(full_url)
    screenshot = driver.get_screenshot_as_png()
    driver.quit()

# Extract Seller Links
seller_link = doc.xpath(xpath_dict["seller_link"])

# Create DataFrame
total_rows = len(seller_name)
if True in map_violation:
    df = pd.DataFrame(
        {
            "Product_Name": np.repeat(product_name, total_rows),
            "ASIN": np.repeat(asin, total_rows),
            "SKU": np.repeat(sku, total_rows),
            "Time_Stamp": np.repeat(time_stamp, total_rows),
            "Seller_Name": seller_name,
            "Seller_URL": seller_link,
            "MAP_Price": np.repeat(map_price, total_rows),
            "Current_Price": original_price,
            "Discount": discount,
            "MAP_Violation": map_violation,
            "Screenshot": np.repeat(screenshot, total_rows),
        }
    )
else:
    df = pd.DataFrame(
        {
            "Product_Name": np.repeat(product_name, total_rows),
            "ASIN": np.repeat(asin, total_rows),
            "SKU": np.repeat(sku, total_rows),
            "Time_Stamp": np.repeat(time_stamp, total_rows),
            "Seller_Name": seller_name,
            "Seller_URL": seller_link,
            "MAP_Price": np.repeat(map_price, total_rows),
            "Current_Price": original_price,
            "Discount": discount,
            "MAP_Violation": map_violation,
        }
    )

return df
