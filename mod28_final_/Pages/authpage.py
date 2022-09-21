import time
from selenium.webdriver.common.by import By
from Locators.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from usefull_methods import check_exists_by_xpath


class AuthorizationPage(object):
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.unauthorized_messages = Locators.unauthorized_messages
        self.no_unauthorized_messages = Locators.no_unauthorized_messages
        self.my_lab = Locators.my_lab
        self.go_to_authorize = Locators.go_to_authorize
        self.hold_over_stash = Locators.hold_over_stash
        self.cart = Locators.cart
        self.discount_code_field = Locators.discount_code_field
        self.button_auth = Locators.button_auth
        self.wrong_discount_code = Locators.wrong_discount_code

    def visible_unauthorized_messages(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.unauthorized_messages))
        actions.perform()
        if check_exists_by_xpath(self.driver, self.unauthorized_messages):
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.unauthorized_messages)))
        else:
            if check_exists_by_xpath(self.driver, self.no_unauthorized_messages):
                self.driver.find_elements(By.XPATH, self.no_unauthorized_messages)

    def visible_my_lab_go_to_authorize(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()

    def click_hold_over(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.hold_over_stash)))
        self.driver.find_element(By.XPATH, self.hold_over_stash).click()

    def click_unauthorized_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.cart)))
        self.driver.find_element(By.XPATH, self.cart).click()

    def click_true_discount_code(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('A748-421E-8B0D')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        time.sleep(30)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab))
        self.driver.find_element(By.XPATH, self.my_lab).click()

    def click_wrong_discount_code(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_lab)))
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH, self.my_lab)).click()
        actions.perform()
        self.driver.find_element(By.XPATH, self.discount_code_field).clear()
        actions.move_to_element(self.driver.find_element(By.XPATH, self.discount_code_field))
        self.driver.find_element(By.XPATH, self.discount_code_field).send_keys('A748-421E-8B0D')
        actions.move_to_element(self.driver.find_element(By.XPATH, self.button_auth))
        self.driver.find_element(By.XPATH, self.button_auth).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.wrong_discount_code)))


