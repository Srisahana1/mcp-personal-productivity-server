"""MCP Personal Productivity Server."""

from mcp.server.fastmcp import FastMCP

from productivity_mcp.database.db import initialize_database

from productivity_mcp.tools.tasks import (
    complete_task as complete_task_db,
    create_task as create_task_db,
    delete_task as delete_task_db,
    list_tasks as list_tasks_db,
)

from productivity_mcp.tools.notes import (
    create_note as create_note_db,
    search_notes as search_notes_db,
)


# Create the MCP server
mcp = FastMCP("Personal Productivity Server")


# -------------------------
# Task Tools
# -------------------------

@mcp.tool()
def create_task(
    title: str,
    description: str = "",
    priority: str = "medium",
    due_date: str | None = None,
) -> dict:
    """Create a new productivity task."""
    return create_task_db(
        title,
        description,
        priority,
        due_date,
    )


@mcp.tool()
def list_tasks(
    include_completed: bool = False,
) -> list[dict]:
    """List productivity tasks."""
    return list_tasks_db(include_completed)


@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark a task as completed."""
    return complete_task_db(task_id)


@mcp.tool()
def delete_task(task_id: int) -> dict:
    """Delete a task."""
    return delete_task_db(task_id)


# -------------------------
# Notes Tools
# -------------------------

@mcp.tool()
def create_note(
    title: str,
    content: str,
) -> dict:
    """Create and save a new note."""
    return create_note_db(title, content)


@mcp.tool()
def search_notes(query: str) -> list[dict]:
    """Search saved notes by title or content."""
    return search_notes_db(query)


# -------------------------
# Start Server
# -------------------------

if __name__ == "__main__":
    initialize_database()
    mcp.run()
