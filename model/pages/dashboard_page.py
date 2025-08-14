import allure
from selene import browser, have, be


class AddTaskButton:
    # --- Locators ---
    DROPDOWN_ITEM = '.dropdown-item.d-flex.px-2.py-1'
    MODAL_HEADER = '.task-purple-modal-headings'
    TASK_TITLE_INPUT = '[placeholder="Add a title"]'
    TASK_ITEM = '.task-item'
    ADD_TASK_BUTTON = '#create-task-btn'

    def __init__(self):
        pass

    # --- Element getters ---

    @property
    def add_task_btn(self):
        return browser.element(self.ADD_TASK_BUTTON)

    @property
    def dropdown_items(self):
        return browser.all(self.DROPDOWN_ITEM)

    @property
    def habit_btn(self):
        return self.dropdown_items.element_by(have.text('Habit'))

    @property
    def daily_btn(self):
        return self.dropdown_items.element_by(have.text('Daily'))

    @property
    def to_do_btn(self):
        return self.dropdown_items.element_by(have.text('To Do'))

    @property
    def reward_btn(self):
        return self.dropdown_items.element_by(have.text('Reward'))

    def modal_with_title(self, title):
        return browser.all(self.MODAL_HEADER).element_by(have.text(title))

    @property
    def title_input(self):
        return browser.element(self.TASK_TITLE_INPUT)

    @property
    def create_btn(self):
        return browser.all('button').element_by(have.text('Create'))

    @property
    def tasks_items(self):
        return browser.all(self.TASK_ITEM)

    # --- Actions ---

    @allure.step("Click on AddTask btn")
    def click_add_task_btn(self):
        self.add_task_btn.click()
        self.dropdown_items.should(have.size_greater_than(0))

    @allure.step("Open modal to create Habit")
    def pick_habit(self):
        self.habit_btn.click()
        self.modal_with_title('Create Habit').should(be.visible)

    @allure.step("Open modal to create Daily")
    def pick_daily(self):
        self.daily_btn.click()
        self.modal_with_title('Create Daily').should(be.visible)

    @allure.step("Open modal to create To Do")
    def pick_to_do(self):
        self.to_do_btn.click()
        self.modal_with_title('Create To Do').should(be.visible)

    @allure.step("Open modal to create Reward")
    def pick_reward(self):
        self.reward_btn.click()
        self.modal_with_title('Create Reward').should(be.visible)

    @allure.step("Add a title to the task")
    def name_a_task(self, value):
        self.title_input.should(be.visible).set_value(value)
        self.create_btn.with_(timeout=5).should(be.enabled)

    @allure.step("Click on the Create btn")
    def click_create_btn(self):
        self.create_btn.click()

    @allure.step("Check if the task was created successfully")
    def check_task_in_list(self, value):
        self.tasks_items.with_(timeout=15).should(
            lambda elements: any(value in el.text for el in elements)
        )
