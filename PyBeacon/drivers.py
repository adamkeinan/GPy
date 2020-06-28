def start(self):
    options = webdriver.ChromeOptions()
    if self.agent:
        options.add_argument("user-agent={}".format(self.agent))
    if self.profile_path:
        options.add_argument("user-data-dir={}".format(self.profile_path))
    if self.headless:
        options.add_argument("--headless")

    # Disables notifications in the Chrome instance to be opened.
    options.add_argument("--disable-notifications")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    chromedriver_path = helper.find_executable("chromedriver")
    if chromedriver_path:
        self._driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
    else:
        self._driver = webdriver.Chrome(chrome_options=options)
