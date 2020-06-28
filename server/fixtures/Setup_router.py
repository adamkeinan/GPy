def setup_router(username: str, password: str, ssid: str):
    """ Execute all setup tasks. """
    logging.debug(f"Initializing webdriver ...")
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(desired_capabilities=options.to_capabilities())
    driver.implicitly_wait(10)

    logging.debug(f'Logging in as user "{username}" ...')
    if not login(driver, username, password):
        logging.error(f"Failed to log in.")
        return
    logging.debug("Login succeeded.")

    logging.debug(f"Changing SSID to {ssid} ...")
    change_ssid(driver, ssid)  # Perform this task last
    driver.quit()
