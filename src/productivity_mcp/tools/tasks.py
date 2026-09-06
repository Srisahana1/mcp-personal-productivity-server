"""Task management functions for the MCP Personal Productivity Server."""

from productivity_mcp.database.db import get_connection


def create_task(
    title: str,
    description: str = "",
    priority: str = "medium",
    due_date: str | None = None,
) -> dict:
    """Create a new productivity task."""

    valid_priorities = {"low", "medium", "high"}

    priority = priority.lower()

    if priority not in valid_priorities:
        return {
            "success": False,
            "message": "Priority must be low, medium, or high.",
        }

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, priority, due_date)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, priority, due_date),
    )

    task_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "success": True,
        "task_id": task_id,
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "message": f"Task '{title}' created successfully.",
    }


def list_tasks(include_completed: bool = False) -> list[dict]:
    """Return tasks stored in the productivity database."""

    connection = get_connection()
    cursor = connection.cursor()

    if include_completed:
        cursor.execute(
            """
            SELECT * FROM tasks
            ORDER BY completed ASC, created_at DESC
            """
        )
    else:
        cursor.execute(
            """
            SELECT * FROM tasks
            WHERE completed = 0
            ORDER BY created_at DESC
            """
        )

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]


def complete_task(task_id: int) -> dict:
    """Mark a task as completed."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
        """,
        (task_id,),
    )

    updated = cursor.rowcount
    connection.commit()
    connection.close()

    if updated == 0:
        return {
            "success": False,
            "message": f"Task {task_id} was not found.",
        }

    return {
        "success": True,
        "task_id": task_id,
        "message": f"Task {task_id} completed successfully.",
    }


def delete_task(task_id: int) -> dict:
    """Delete a task."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,),
    )

    deleted = cursor.rowcount
    connection.commit()
    connection.close()

    if deleted == 0:
        return {
            "success": False,
            "message": f"Task {task_id} was not found.",
        }

    return {
        "success": True,
        "task_id": task_id,
        "message": f"Task {task_id} deleted successfully.",
    }
