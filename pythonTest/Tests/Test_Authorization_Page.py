from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""В целях экономии времени не буду задействовать фикструры и сильно углубляться в ооп и явные/неявные ожидания, 
хотя умею этим пользоваться"""


def test_invalid_email_authentication(self):
    # Создаю вебдрайвер для хрома и в настройках указываю, чтоб он не закрывался после выполнения кода.
    chrom_options = Options()
    chrom_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrom_options)

    # Создаю поля, которые буду использовать в тестах.
    authorization_page_url = "https://www.ourapp.com/authorization_page"  # Урла страницы регистрации нашего приложения.
    error_message = "Неверный имейл"

    name = "Artyom"
    surname = "Avdieiev"
    email = "@mail.com"
    phone_number = 89810147436

    # Перешёл на страницу регистрации
    driver.get(authorization_page_url)
    driver.implicitly_wait(3)

    # Ищу поля ввода, чекбокс и кнопку регистрации.
    name_input_line_xpath = driver.find_element(By.XPATH, "some xpath")
    surname_input_line_xpath = driver.find_element(By.XPATH, "some xpath")
    email_input_line_xpath = driver.find_element(By.XPATH, "some xpath")
    phone_number_input_line_xpath = driver.find_element(By.XPATH, "some xpath")
    check_box_xpath = driver.find_element(By.XPATH,
                                          "some xpath")  # Тут я возьму координаты xpath для чекбокса из браузера.
    auth_button_xpath = driver.find_element(By.XPATH,
                                            "some xpath")  # Тут я возьму координаты xpath для кнопки регистрации.

    # Ввожу значения в поля ввода.
    name_input_line_xpath.send_keys(name)
    surname_input_line_xpath.send_keys(surname)
    email_input_line_xpath.send_keys(email)
    phone_number_input_line_xpath.send_keys(phone_number)
    check_box_xpath.click()
    auth_button_xpath.click()

    assert driver.current_url == authorization_page_url  # проверели, что перешли на нужную урлу.
    assert driver.find_element(By.XPATH, "сообщение об ошибке")
    assert driver.find_element(By.XPATH, "сообщение об ошибке").text == error_message

