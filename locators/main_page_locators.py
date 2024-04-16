from selenium.webdriver.common.by import By


class HeadersLocators:
    ACCOUNT_LINK = By.XPATH, '//*[@href="/account"]'  # ссылка Личный кабинет в хэдере
    CONSTRUCTOR_LINK = By.XPATH, '//p[text()="Конструктор"]/parent::a'  # ссылка Конструктор в хэдере
    ORDER_LIST_LINK = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'  # ссылка Лента Заказов в хэдере


class MainPageLocators:
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти в аккаунт"]'
    CONSTRUCTOR_TITLE = By.XPATH, '//h1[text()="Соберите бургер"]'  # заголовок Соберите бургер
    ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'  # кнопка Оформить заказ

    SAUCES = By.XPATH, '//span[text()="Соусы"]/parent::div'  # раздел Соусы
    FILLING = By.XPATH, '//span[text()="Начинки"]/parent::div'  # раздел Начинки
    BREAD = By.XPATH, '//span[text()="Булки"]/parent::div'  # раздел Булки

    INGREDIENT_BUN = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]' #ингредиент Флюоресцентная булка R2-D3
    INGREDIENT_FILLING = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]' #ингредиент Мясо бессмертных моллюсков Protostomia
    INGREDIENT_SAUCE = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]' #ингредиент Соус фирменный Space Sauce
    INGREDIENT_COUNTER = By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]' #счетчик ингредиента Флюоресцентная булка
    INGREDIENT_POPUP_TITLE = By.XPATH, '//h2[text()="Детали ингредиента"]' # заголовок всплывающего окна Детали ингредиента
    INGREDIENT_POPUP = By.XPATH, '//*[contains(@class, "contentBox")]'  # всплывающее окно Детали ингредиента
    ORDER_BASKET = By.XPATH, '//ul[contains(@class,"basket")]'  #Корзина
    ORDER_NUMBER = By.XPATH, '//*[contains(@class, "type_digits-large")]' # номер заказа во всплывающем окне
    DEFAULT_ORDER = By.XPATH, '//h2[text()="9999"]' #дефолтный номер заказа в попапе
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]' #Ваш заказ начали готовить в попапе
    CLOSE_BUTTON = By.XPATH, '//button[contains(@class,"close")]' #Крестик закрытия всплывающего окна
