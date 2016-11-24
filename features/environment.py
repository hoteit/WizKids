from selenium.webdriver import Chrome
from wizkids.settings import CHROME_PATH

def before_all(context):
    context.browser = Chrome(executable_path=CHROME_PATH)

def after_all(context):
    context.browser.quit()
    context.browser = None


