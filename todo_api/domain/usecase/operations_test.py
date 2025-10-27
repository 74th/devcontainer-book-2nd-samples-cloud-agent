from unittest import TestCase
from todo_api.domain.entity.entity import Task

from todo_api.memdb.memdb import MemDB
from .operations import OperationInteractor

class OperationTest(TestCase):

    def test_task_work(self):
        db = MemDB()
        op = OperationInteractor(db)

        tasks = op.show_tasks()

        assert len(tasks) >0, "初期状態のリポジトリからはタスクが引けること"

        new_task = Task(
            id=None,
            text="new task",
            done=False,
        )
        created_task = op.create_task(new_task)

        assert created_task["id"] is not None, "タスクIDが割り振られること"

    def test_delete_task(self):
        db = MemDB()
        op = OperationInteractor(db)

        initial_tasks = op.show_tasks()
        initial_count = len(initial_tasks)

        op.delete_task(0)

        remaining_tasks = op.show_tasks()
        assert len(remaining_tasks) == initial_count - 1, "タスクが削除されること"
