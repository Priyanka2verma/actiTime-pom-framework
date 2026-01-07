from generic.assertion import verify_text
from generic.verification import verify_title
from pom.home_page import HomePage
from pom.login_page import LoginPage
from pom.create_new_task import CreateNewTask

def test_testcase3(launch):
    driver = launch
    verify_title(driver, "actiTIME - Login")
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h = HomePage(driver)
    h.select_user("automation, selenium (seleniumauto)")
    verify_title(driver, "actiTIME - Enter Time-Track")
    h.new_link()
    verify_title(driver, "actiTIME - Create New Tasks")
    c = CreateNewTask(driver)
    c.customer_name("ICICI Bank")
    c.project_name("mobile application")
    c.task_name("write test scenario and testcase")
    c.estimate_time(9)
    c.create_task()
    verify_text(driver, "write test scenario and testcase")
    h.logout_link()
    verify_title(driver, "actiTIME - Login")
    l.username("seleniumauto")
    l.password("selenium@123")
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    c.user_time(9)
    c.save_changes()
    h.logout_link()
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h.select_user("automation, selenium (seleniumauto)")
    verify_text(driver, "9")


