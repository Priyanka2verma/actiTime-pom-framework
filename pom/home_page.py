class HomePage:
    def __init__(self,driver):
        self.driver = driver
    def logout_link(self):
        self.driver.find_element("id", "logoutLink").click()
    def users_tab(self):
        self.driver.find_element("xpath", "//div[text()='Users']").click()
    def select_user(self, data):
        self.driver.find_element("id", "ext-gen7").click()
        self.driver.find_element("xpath", f"//div[text()='{data}']").click()
    def new_link(self):
        self.driver.find_element("xpath", "//a[text()='New']").click()
        allid = self.driver.window_handles
        self.driver.switch_to.window(allid[1])

