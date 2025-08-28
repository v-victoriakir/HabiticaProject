import pytest
import allure
from allure_commons.types import Severity

pytestmark = [
    allure.label('layer', 'api'),
    allure.suite('API'),
]

@allure.tag('API')
@allure.feature("Task Operations")
@allure.label('owner', 'Victoria K')
class TestTaskManagement:

    @allure.title('Test task lifecycle: create → verify type → verify text → delete')
    @allure.severity(Severity.CRITICAL)
    def test_complete_task_lifecycle(self, tasks_api):
        # 1. Создание задач разных типов со случайными текстами
        with allure.step("Create multiple tasks with different types and random texts"):
            habit_task = tasks_api.create_task(task_type="habit")
            todo_task = tasks_api.create_task(task_type="todo")
            daily_task = tasks_api.create_task(task_type="daily")
            reward_task = tasks_api.create_task(task_type="reward")

            print(f"Created tasks: "
                  f"Habit({habit_task['id']}), "
                  f"Todo({todo_task['id']}), "
                  f"Daily({daily_task['id']}), "
                  f"Reward({reward_task['id']})")

        # 2. Проверка типов созданных задач
        with allure.step("Verify task types are correct"):
            tasks_api.verify_task_type(habit_task['id'], "habit")
            tasks_api.verify_task_type(todo_task['id'], "todo")
            tasks_api.verify_task_type(daily_task['id'], "daily")
            tasks_api.verify_task_type(reward_task['id'], "reward")
            print("All task types verified successfully")

        # 3. Проверка текстов задач (что текст не пустой и соответствует формату)
        with allure.step("Verify task texts are correct and not empty"):
            tasks_api.verify_task_text(habit_task['id'], habit_task['text'])
            tasks_api.verify_task_text(todo_task['id'], todo_task['text'])
            tasks_api.verify_task_text(daily_task['id'], daily_task['text'])
            tasks_api.verify_task_text(reward_task['id'], reward_task['text'])
            print("All task texts verified successfully")

        # 4. Удаление задач
        with allure.step("Delete all created tasks"):
            tasks_api.delete_task_by_id(habit_task['id'])
            tasks_api.delete_task_by_id(todo_task['id'])
            tasks_api.delete_task_by_id(daily_task['id'])
            tasks_api.delete_task_by_id(reward_task['id'])
            print("All tasks deleted successfully")

        # 5. Проверка, что задачи удалены
        with allure.step("Verify all tasks are deleted"):
            tasks_api.verify_task_exists(habit_task['id'], False)
            tasks_api.verify_task_exists(todo_task['id'], False)
            tasks_api.verify_task_exists(daily_task['id'], False)
            tasks_api.verify_task_exists(reward_task['id'], False)
            print("All tasks deletion verified successfully")

    @allure.title('Test task lifecycle - parameterized test')
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize("task_type", ["habit", "todo", "daily", "reward"])
    def test_all_task_types_parameterized(self, tasks_api, task_type):
        task = tasks_api.create_task(task_type=task_type)
        tasks_api.verify_task_type(task['id'], task_type)
        assert task['text'].startswith("TestTask_"), \
            f"Task text should start with 'TestTask_': {task['text']}"
        tasks_api.delete_task_by_id(task['id'])
        tasks_api.verify_task_exists(task['id'], False)

    @allure.title('Test task updating')
    @allure.severity(Severity.NORMAL)
    def test_task_updating(self, tasks_api):
        task = tasks_api.create_task(task_type="todo")
        new_text = "Обновленный текст задачи"
        new_notes = "Тестовые заметки"
        new_priority = 2

        with allure.step("Update task properties"):
            updated_task = tasks_api.update_task(
                task['id'],
                text=new_text,
                notes=new_notes,
                priority=new_priority
            )

        with allure.step("Verify task updates"):
            assert updated_task['text'] == new_text, "Task text should be updated"
            assert updated_task['notes'] == new_notes, "Task notes should be updated"
            assert updated_task['priority'] == new_priority, "Task priority should be updated"

        tasks_api.delete_task_by_id(task['id'])

    @allure.title('Test move task to top: create → verify → move to top → verify → delete')
    @allure.severity(Severity.NORMAL)
    def test_move_task_to_top(self, tasks_api):
        # 1. Создание 3 задач одного типа
        with allure.step("Create 3 tasks of 'todo' type with random texts"):
            task3 = tasks_api.create_task(task_type="todo")
            task2 = tasks_api.create_task(task_type="todo")
            task1 = tasks_api.create_task(task_type="todo")

            task_ids = [task1['id'], task2['id'], task3['id']]
            print(f"Created 3 todo tasks: {task_ids}")

        # 2. Проверка типов всех задач
        with allure.step("Verify all tasks have correct 'todo' type"):
            for task_id in task_ids:
                tasks_api.verify_task_type(task_id, "todo")
            print("All tasks have correct 'todo' type")

        # 3. Запоминаем начальный порядок задач
        with allure.step("Check initial task order"):
            all_tasks = tasks_api.get_all_tasks()
            initial_order = [task['id'] for task in all_tasks if task['id'] in task_ids]
            print(f"Initial task order: {initial_order}")

        # 4. Перемещаем задачу 3 в начало (position 0)
        with allure.step("Move task 3 to top (position 0)"):
            tasks_api.move_task_to_position(task3['id'], 0)
            print(f"Moved task {task3['id']} to position 0")

        # 5. Проверяем, что задача 3 теперь первая
        with allure.step("Verify task 3 is now first"):
            updated_tasks = tasks_api.get_all_tasks()
            updated_order = [task['id'] for task in updated_tasks if task['id'] in task_ids]
            print(f"Order after moving to top: {updated_order}")

            assert updated_order[0] == task3['id'], \
                f"Task 3 should be first, but order is: {updated_order}"
            print("Task 3 successfully moved to top")

        # 8. Удаляем все задачи
        with allure.step("Delete all tasks"):
            tasks_api.delete_task_by_id(task1['id'])
            tasks_api.delete_task_by_id(task2['id'])
            tasks_api.delete_task_by_id(task3['id'])
            print("All tasks deleted")

        # 9. Проверяем, что все задачи удалены
        with allure.step("Verify all tasks are deleted"):
            for task_id in task_ids:
                tasks_api.verify_task_exists(task_id, False)
            print("All tasks deletion verified")

    @allure.title('Test move task to bottom: create → verify → move to bottom → verify → delete')
    @allure.severity(Severity.NORMAL)
    def test_move_task_to_bottom(self, tasks_api):
        # 1. Создание 3 задач одного типа
        with allure.step("Create 3 tasks of 'todo' type with random texts"):
            task3 = tasks_api.create_task(task_type="todo")
            task2 = tasks_api.create_task(task_type="todo")
            task1 = tasks_api.create_task(task_type="todo")

            task_ids = [task1['id'], task2['id'], task3['id']]
            print(f"Created 3 todo tasks: {task_ids}")

        # 2. Проверка типов всех задач
        with allure.step("Verify all tasks have correct 'todo' type"):
            for task_id in task_ids:
                tasks_api.verify_task_type(task_id, "todo")
            print("All tasks have correct 'todo' type")

        # 3. Запоминаем начальный порядок задач
        with allure.step("Check initial task order"):
            all_tasks = tasks_api.get_all_tasks()
            initial_order = [task['id'] for task in all_tasks if task['id'] in task_ids]
            print(f"Initial task order: {initial_order}")

        # 4. Перемещаем задачу 1 в конец (position -1)
        with allure.step("Move task 1 to bottom (position -1)"):
            tasks_api.move_task_to_position(task1['id'], -1)
            print(f"Moved task {task1['id']} to position -1")

        # 5. Проверяем, что задача 1 теперь последняя
        with allure.step("Verify task 1 is now last"):
            final_tasks = tasks_api.get_all_tasks()
            final_order = [task['id'] for task in final_tasks if task['id'] in task_ids]
            print(f"Order after moving to bottom: {final_order}")

            assert final_order[-1] == task1['id'], \
                f"Task 1 should be last, but order is: {final_order}"
            print("Task 1 successfully moved to bottom")

        # 8. Удаляем все задачи
        with allure.step("Delete all tasks"):
            tasks_api.delete_task_by_id(task1['id'])
            tasks_api.delete_task_by_id(task2['id'])
            tasks_api.delete_task_by_id(task3['id'])
            print("All tasks deleted")

        # 9. Проверяем, что все задачи удалены
        with allure.step("Verify all tasks are deleted"):
            for task_id in task_ids:
                tasks_api.verify_task_exists(task_id, False)
            print("All tasks deletion verified")

    @allure.title('Test task creation with custom text and type verification')
    @allure.severity(Severity.NORMAL)
    def test_task_creation_with_custom_text(self, tasks_api):
        custom_text = "Важная задача на понедельник"
        task = tasks_api.create_task(task_text=custom_text, task_type="daily")
        tasks_api.verify_task_type(task['id'], "daily")
        tasks_api.verify_task_text(task['id'], custom_text)
        tasks_api.delete_task_by_id(task['id'])
        tasks_api.verify_task_exists(task['id'], False)

