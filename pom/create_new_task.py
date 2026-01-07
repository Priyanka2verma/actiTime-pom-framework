class CreateNewTask:
    def __init__(self, driver):
        self.driver = driver
    def customer_name(self, data):
        self.driver.find_element("name", "customerName").send_keys(data)
    def project_name(self, data):
        self.driver.find_element("name", "projectName").send_keys(data)
    def task_name(self, data):
        self.driver.find_element("id", "task[0].name").send_keys(data)
    def estimate_time(self, data):
        self.driver.find_element("id", "task[0].budgetedTimeStr").send_keys(data)
    def create_task(self):
        self.driver.find_element("xpath", "//input[@value='Create Tasks']").click()
        allid = self.driver.window_handles
        self.driver.switch_to.window(allid[0])
    def user_time(self, data):
        self.driver.find_element("xpath", "//input[@class='text inputTT']").send_keys(data)
    def save_changes(self):
        self.driver.find_element("xpath", "//input[@value='Save Changes']").click()