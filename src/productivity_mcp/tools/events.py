"""Event management functions for the MCP Personal Productivity Server."""

from productivity_mcp.database.db import get_connection


def add_event(
    title: str,
    event_date: str,
    description: str = "",
) -> dict:
    """Create a new event."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO events (title, event_date, description)
        VALUES (?, ?, ?)
        """,
        (title, event_date, description),
    )

    event_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "success": True,
        "event_id": event_id,
        "title": title,
        "event_date": event_date,
        "message": f"Event '{title}' created successfully.",
    }


def list_events() -> list[dict]:
    """Return all saved events."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM events
        ORDER BY event_date ASC, created_at DESC
        """
    )

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]
