def __init__(self, proxy):
    """init the webdriver by setting the proxy and user-agent

	Args:
			proxy (str): proxy in the form of ip:port
	"""
    # reload(sys)
    # sys.setdefaultencoding( "utf-8" )
    # set proxy
    ip, port = proxy.split(":")
    chromedriver = "C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    # driver = webdriver.Chrome(chromedriver)
    profile = webdriver.ChromeOptions()
    # profile.add_argument('--proxy-server=http://"%s":"%s"' %(ip, port))
    self.driver = webdriver.Chrome(chromedriver, chrome_options=profile)
    # set user_agent
    # profile.set_preference("general.useragent.override", generate_user_agent())

    # profile.update_preferences()
    # self.driver = webdriver.Firefox(firefox_profile=profile)

    print
    "current proxy: %s" % (proxy)
