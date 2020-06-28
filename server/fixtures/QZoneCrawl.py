def __init__(self, qq, timeout=20, save_images=True, driver="Phantomjs"):
    socket.setdefaulttimeout(timeout)
    self.qq = qq
    self.__login = False
    self.save_images = save_images
    self.userAgent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 "
        ""
        "(KHTML, like Gecko) "
        "Chrome/61.0.3163.100 Safari/537.36 "
    )
    self.md = (
        "此({})动态由https://github.com/netcan/QZoneCrawler于{" "}采集备份，欢迎Star/交流学习，禁止商用。\n\n"
    )
    if driver == "Phantomjs":
        opt = dict(DesiredCapabilities.PHANTOMJS)
        opt["phantomjs.page.settings.userAgent"] = self.userAgent
        self.driver = webdriver.PhantomJS(desired_capabilities=opt)
    else:
        opt = webdriver.ChromeOptions()
        opt.add_argument("user-agent=" + self.userAgent)
        self.driver = webdriver.Chrome(chrome_options=opt)
