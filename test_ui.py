import allure

from selenium.webdriver.common.by import By


@allure.title("Тест forgot password")
def test_forgot_password(driver):

    driver.get(
        "https://the-internet.herokuapp.com/forgot_password"
    )

    driver.find_element(
        By.ID,
        "email"
    ).send_keys("test@test.com")

    driver.find_element(
        By.ID,
        "form_submit"
    ).click()

    # Навмисна помилка
    assert False