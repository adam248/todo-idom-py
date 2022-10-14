from uuid import uuid4


class TodoList:
    def __init__(self):
        self.tasks = [
            {"id": 0, "text": "Make breakfast", "priority": 0, "done": True},
            {"id": 1, "text": "Feed the dog", "priority": 0},
            {"id": 2, "text": "Do laundry", "priority": 2},
            {"id": 3, "text": "Go on a run", "priority": 1},
            {"id": 4, "text": "Clean the house", "priority": 2},
            {"id": 5, "text": "Go to the grocery store", "priority": 2},
            {"id": 6, "text": "Do some coding", "priority": 1},
            {"id": 7, "text": "Read a book", "priority": 1},
        ]
        self.generate_ids_for_tasks()
        self.set_all_tasks_to_undone()

    def generate_ids_for_tasks(self):
        for task in self.tasks:
            task["id"] = uuid4().hex

    def set_all_tasks_to_undone(self):
        for task in self.tasks:
            if task.get("done", None) is None:
                task["done"] = False

    @staticmethod
    def add_task(task: str):
        return {"id": uuid4().hex, "text": task, "priority": 0, "done": False}
