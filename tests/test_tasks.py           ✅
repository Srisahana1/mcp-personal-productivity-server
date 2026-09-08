from productivity_mcp.database.db import initialize_database
from productivity_mcp.tools.tasks import (
    create_task,
    list_tasks,
    complete_task,
    delete_task,
)


def test_task_lifecycle(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    initialize_database()

    created = create_task(
        title="Test task",
        description="Testing task lifecycle",
        priority="high",
        due_date="2026-09-08",
    )

    assert created["success"] is True
    task_id = created["task_id"]

    tasks = list_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task"
    assert tasks[0]["completed"] == 0

    completed = complete_task(task_id)

    assert completed["success"] is True

    active_tasks = list_tasks()

    assert active_tasks == []

    all_tasks = list_tasks(include_completed=True)

    assert len(all_tasks) == 1
    assert all_tasks[0]["completed"] == 1

    deleted = delete_task(task_id)

    assert deleted["success"] is True

    remaining = list_tasks(include_completed=True)

    assert remaining == []
