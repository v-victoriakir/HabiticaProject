import allure
from selene import browser, have, be


class AddTaskButton:
    # --- Locators ---
    ADD_TASK_BUTTON = '#create-task-btn'
    DROPDOWN_TASK_ITEMS = '.dropdown-item.d-flex.px-2.py-1'
    MODAL_HEADER = '.task-purple-modal-headings'
    TASK_TITLE_INPUT = '[placeholder="Add a title"]'
    CREATE_BTN = 'button'
    TASKS_LIST = '.tasks-list'
    TASK_ITEM = '.task-item'

    def __init__(self):
        pass

    # --- Element getters ---

    def add_task_btn(self):
        return browser.element(self.ADD_TASK_BUTTON)

    def dropdown_items(self):
        return browser.all(self.DROPDOWN_TASK_ITEMS)

    def modal_header(self):
        return browser.all(self.MODAL_HEADER)

    def title_input(self):
        return browser.element(self.TASK_TITLE_INPUT)

    def create_btn(self):
        return browser.all('button').element_by(have.text('Create'))

    def tasks_items(self):
        return browser.all(self.TASK_ITEM)

    # --- Actions ---

    @allure.step("Click on AddTask btn")
    def click_add_task_btn(self):
        self.add_task_btn().click()
        self.dropdown_items().should(have.size_greater_than(0))

    @allure.step('Open modal to create task: {task_type}')
    def pick_task(self, task_type: str):
        self.dropdown_items().element_by(have.text(task_type)).should(be.visible).click()
        self.modal_header().element_by(have.exact_text(f'Create {task_type}')).should(be.visible)

    @allure.step("Add a title to the task")
    def name_a_task(self, value):
        self.title_input().should(be.visible).set_value(value)
        self.create_btn().with_(timeout=5).should(be.enabled)

    @allure.step("Click on the Create btn")
    def click_create_btn(self):
        self.create_btn().click()

    @allure.step("Check if the task was created successfully")
    def check_task_in_list(self, value):
        self.tasks_items().with_(timeout=15).should(
            lambda elements: any(value in el.text for el in elements)
        )


class ProfileMenu:
    # --- Locators ---
    PROFILE_MENU_TOGGLE = 'div.habitica-menu-dropdown[role="button"] div.habitica-menu-dropdown-toggle'
    DROPDOWN_MENU_ITEMS = 'a.topbar-dropdown-item'
    MENU_CONTAINER = 'div.habitica-menu-dropdown.dropdown.item-user'
    DROPDOWN_MENU = 'div.dropdown-menu.dropdown-menu-right'

    def __init__(self):
        pass

    # --- Element getters ---

    def profile_menu_toggle(self):
        return browser.element(self.PROFILE_MENU_TOGGLE)

    def profile_menu_items(self):
        return browser.all(self.DROPDOWN_MENU_ITEMS)

    @allure.step("Open profile menu")
    def open_profile_menu(self):
        browser.element(self.MENU_CONTAINER).with_(timeout=10).should(be.present)
        self.profile_menu_toggle().with_(timeout=10).should(be.visible)

        try:
            self.profile_menu_toggle().click()
        except Exception:
            browser.execute_script("arguments[0].click();", self.profile_menu_toggle())

        browser.element(self.DROPDOWN_MENU).with_(timeout=5).should(be.visible)
        self.profile_menu_items().should(have.size_greater_than(0))

    @allure.step("Click on a menu item")
    def click_menu_item(self, value: str):
        self.profile_menu_items().element_by(have.text(value)).should(be.visible).click()
