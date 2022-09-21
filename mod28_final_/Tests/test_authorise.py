from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.authpage import AuthorizationPage


class TestAuthorizationPage:
    # Клиентский блок неавторизованного пользователя.
    def test_visible_unauthorized_messages(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.visible_unauthorized_messages()

    def test_visible_my_lab_go_to_authorize(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.visible_my_lab_go_to_authorize()
        assert driver.find_element(
            By.XPATH, "//span[contains(text(), 'Введите свой код скидки, телефон или эл.почту')]").is_displayed()

    def test_click_hold_over(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1300, 700)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_hold_over()
        assert driver.current_url == 'https://www.labirint.ru/cabinet/putorder/'

    def test_unauthorized_cart(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1800, 1200)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_unauthorized_cart()
        assert driver.current_url == 'https://www.labirint.ru/cart/'

    # АВТОРИЗАЦИЯ по коду скидки.
    def test_true_discount_code(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1800, 1200)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_true_discount_code()
        assert driver.find_element(By.XPATH, "//span[contains(text(), ' Код скидки A748-421E-8B0D')]").is_displayed()

    def test_wrong_discount_code(self):
        driver = webdriver.Chrome(executable_path='C:\\Users\\игорь\\PycharmProjects\\mod28_final_\\chromedriver.exe')
        driver.set_window_size(1800, 1200)
        driver.get('https://www.labirint.ru/')
        homepage = AuthorizationPage(driver)
        homepage.click_wrong_discount_code()
        assert driver.find_element(By.XPATH, '//*[@id="auth-by-code"]/div[3]/span[3]/small[1]').is_displayed()
