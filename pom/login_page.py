class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def username(self, data):
        self.driver.find_element("id", "username").send_keys(data)
    def password(self, data):
        self.driver.find_element("name", "pwd").send_keys(data)
    def login_button(self):
        self.driver.find_element("id", "loginButton").click()











