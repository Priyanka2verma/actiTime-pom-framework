from generic.take_screenshot import screenshot
from time import sleep

def verify_text(driver, etext):
    sleep(2)
    try:
        assert etext in driver.page_source, "Text not matches"
    except:
        screenshot(driver)
        raise Exception("Title Not Matches")

