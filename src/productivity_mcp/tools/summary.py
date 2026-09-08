"""Daily productivity summary functions."""

from datetime import date

from productivity_mcp.database.db import get_connection


def daily_summary(summary_date: str | None = None) -> dict:
    """Return tasks and events for a specific day."""

    target_date = summary_date or date.today().isoformat()

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM tasks
        WHERE completed = 0
        AND due_date = ?
        ORDER BY priority DESC, created_at DESC
        """,
        (target_date,),
    )

    tasks = [dict(row) for row in cursor.fetchall()]

    cursor.execute(
        """
        SELECT *
        FROM events
        WHERE event_date = ?
        ORDER BY created_at DESC
        """,
        (target_date,),
    )

    events = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return {
        "date": target_date,
        "pending_tasks": tasks,
        "events": events,
        "task_count": len(tasks),
        "event_count": len(events),
    }
