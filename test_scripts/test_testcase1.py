from generic.verification import verify_title
from pom.login_page import LoginPage
from pom.home_page import HomePage

def test_testcase1(launch):
    driver = launch
    verify_title(driver, "actiTIME - Login")
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h = HomePage(driver)
    h.logout_link()
    verify_title(driver, "actiTIME - Login")







