"""Notes management functions for the MCP Personal Productivity Server."""

from productivity_mcp.database.db import get_connection


def create_note(title: str, content: str) -> dict:
    """Create a new note."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO notes (title, content)
        VALUES (?, ?)
        """,
        (title, content),
    )

    note_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return {
        "success": True,
        "note_id": note_id,
        "title": title,
        "message": f"Note '{title}' created successfully.",
    }


def search_notes(query: str) -> list[dict]:
    """Search notes by title or content."""

    connection = get_connection()
    cursor = connection.cursor()

    search_term = f"%{query}%"

    cursor.execute(
        """
        SELECT * FROM notes
        WHERE title LIKE ? OR content LIKE ?
        ORDER BY created_at DESC
        """,
        (search_term, search_term),
    )

    rows = cursor.fetchall()
    connection.close()

    return [dict(row) for row in rows]
