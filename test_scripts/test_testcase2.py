from generic.verification import verify_title
from pom.home_page import HomePage
from pom.login_page import LoginPage
from pom.user_list_page import UserListPage
from generic.assertion import verify_text
from generic.excel_read import read_data

data = read_data()          #data=[un,pwd,..]
def test_testcase2(launch):
    driver = launch
    verify_title(driver, "actiTIME - Login")
    l = LoginPage(driver)
    l.username(data[0])
    l.password(data[1])
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h = HomePage(driver)
    h.users_tab()
    verify_title(driver, "actiTIME - User List")
    u = UserListPage(driver)
    u.user_button()
    verify_text(driver, "Create New User")
    u.first_name(data[2])
    u.last_name(data[3])
    u.email(data[4])
    u.user_name(data[5])
    u.password(data[6])
    u.retype_password(data[7])
    u.create_user_button()
    verify_text(driver, "automation, selenium (seleniumauto)")
    h.logout_link()
    verify_title(driver, "actiTIME - Login")
    l.username("seleniumauto")
    l.password("selenium@123")
    l.login_button()
    verify_title(driver, "actiTIME - Enter Time-Track")
    h.logout_link()
    verify_title(driver, "actiTIME - Login")





































