from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui




class TestYandexAuthorization():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.wait = ui.WebDriverWait(self.driver,10)

    def test_auth(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://passport.yandex.ru/auth")
        email = driver.find_element(by=By.CLASS_NAME,
                                    value='Textinput-Control')
        em = '' # впишите свой email до @yandex.ru
        email.send_keys(em)
        button_to_enter = driver.find_element(by=By.ID,value='passp:sign-in')
        button_to_enter.click()
        wait.until(lambda driver: driver.find_element(by=By.ID,value='passp-field-passwd'))
        passwd = driver.find_element(by=By.ID,value='passp-field-passwd')
        password = '' # напишите пароль от аккаунта Яндекс
        passwd.send_keys(password)
        button_to_continue = driver.find_element(by=By.ID,value='passp:sign-in')
        button_to_continue.click()
        wait.until(lambda driver: driver.find_element(by=By.ID,value='react-aria-13'))
        user_name = driver.find_element(by=By.ID,value='react-aria-13')

        your_first_and_last_name = '' # напишите Ваши имя и фамилию через пробел, которые указаны в профиле под аватаром
        assert user_name.text == your_first_and_last_name

    def teardown_class(self):
        self.driver.close()
