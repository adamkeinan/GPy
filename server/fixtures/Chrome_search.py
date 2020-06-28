def browser_init():
    """
	Initialize browser

	:return:
	"""
    system_version = platform.system().upper()
    browser_bin = ""
    parent = os.path.dirname(os.path.abspath(__file__))
    if system_version.startswith("LINUX"):
        browser_bin = os.path.join(parent, "drivers", "chromedriver-linux")
    if system_version.startswith("WINDOWS"):
        browser_bin = os.path.join(parent, "drivers", "chromedriver.exe")
    if system_version.startswith("DARWIN"):
        browser_bin = os.path.join(parent, "drivers", "chromedriver-mac")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--enable-automation")
    browser = webdriver.Chrome(browser_bin, chrome_options=chrome_options)
    browser.get("http://www.baidu.com")
    return browser
