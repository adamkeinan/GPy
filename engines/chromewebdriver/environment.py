## Chromium WebDriver
## https://sites.google.com/a/chromium.org/chromedriver/capabilities#TOC-Using-a
## -Chrome-executable-in-a-non-standard-location


def selenium_browser_chrome(context):
    # start the browser
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920,1080")

    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["acceptSslCerts"] = True
    capabilities["acceptInsecureCerts"] = True

    context.browser = webdriver.Chrome(
        chrome_options=chrome_options, desired_capabilities=capabilities
    )
    yield context.browser

    # clean up
