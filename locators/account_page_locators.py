from selenium.webdriver.common.by import By


class AuthPageLocators:
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]'  #кнопка Войти на странице авторизации
    RESET_PASSWORD_LINK = By.XPATH, '//*[@href="/forgot-password"]'  #ссылка Восстановить пароль на странице авторизации
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода емейла
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля


class AccountPageLocators:
    PROFILE_LINK = By.XPATH, '//*[@href="/account/profile"]'  # cсылка Профиль в ЛК
    ORDER_HISTORY_LINK = By.XPATH, '//*[@href="/account/order-history"]'  # cсылка История заказов в ЛК
    EXIT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка Выход
    ORDER_STATUS = By.XPATH, '//p[text()="Выполнен"]'  # статус заказа в Истории заказов
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'  #номер заказа в Личном кабинете


class PasswordResetPageLocators:
    RESET_BUTTON = By.XPATH, '//button[text()="Восстановить"]'  # кнопка Восстановить
    SAVE_BUTTON = By.XPATH, '//button[text()="Сохранить"]'  # кнопка Сохранить
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class,"icon-action")]' #кнопка Показать/скрыть пароль
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'  # поле ввода емейла
    INPUT_PASSWORD = By.XPATH, '//input[@type="password"]'  # поле ввода пароля
    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'  #поле Пароль активно
