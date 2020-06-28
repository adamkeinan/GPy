def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-gpu")
    options.add_argument("headless")
    options.add_argument("no-default-browser-check")
    options.add_argument("no-first-run")
    options.add_argument("no-sandbox")

    d = DesiredCapabilities.CHROME
    d["loggingPrefs"] = {"browser": "ALL"}

    driver = webdriver.Chrome(options=options, desired_capabilities=d)
    driver.implicitly_wait(30)

    yield driver
    driver.quit()
