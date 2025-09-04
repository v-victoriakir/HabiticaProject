import allure
from selene import browser, have, be

class AddTaskButton:
    def __init__(self):
        self.add_task_btn = browser.element('#create-task-btn')
        self.dropdown_items = browser.all('.dropdown-item.d-flex.px-2.py-1')
        self.modal_header = browser.element('.task-modal-header')
        self.title_input = browser.element('.input-title.task-purple-modal-input')
        self.create_button = browser.element('button.btn-primary.btn-footer')
        self.tasks_items = browser.all('.task-item')

    @allure.step("Click on AddTask btn")
    def click_add_task_btn(self):
        self.add_task_btn.click()

    @allure.step('Open modal to create task type by index: {index}')
    def pick_task_by_index(self, index: int):
        self.dropdown_items.should(have.size_greater_than_or_equal(index + 1))
        self.dropdown_items[index].should(be.visible).click()
        self.modal_header.should(be.visible)

    @allure.step("Add a title to the task")
    def name_a_task(self, value):
        self.title_input.should(be.visible).set_value(value)
        self.create_button.with_(timeout=5).should(be.enabled)

    @allure.step("Click on the Create btn")
    def click_create_btn(self):
        self.create_button.should(be.clickable).click()

    @allure.step("Check if the task was created successfully")
    def check_task_in_list(self, value):
        self.tasks_items.with_(timeout=15).should(
            lambda elements: any(value in el.text for el in elements)
        )
