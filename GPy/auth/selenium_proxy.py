def _get_web_driver(self, headless):
    user_agent = """
            Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko)
            Chrome/60.0.3112.50 Safari/537.36
        """

    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("headless")
    if os.getenv("MYCLOUD_DOCKER"):
        chrome_options.add_argument("no-sandbox")
    proxy_str = "--proxy-server=http://{0}:{1}".format(PROXY_HOST, str(PROXY_PORT))
    chrome_options.add_argument(proxy_str)
    chrome_options.add_argument("user-agent={0}".format(user_agent))
    driver = webdriver.Chrome(CHROME_DRIVER, chrome_options=chrome_options)

    self._driver = driver
