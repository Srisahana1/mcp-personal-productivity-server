from productivity_mcp.database.db import initialize_database
from productivity_mcp.tools.events import add_event, list_events
from productivity_mcp.tools.notes import create_note, search_notes
from productivity_mcp.tools.summary import daily_summary
from productivity_mcp.tools.tasks import create_task


def test_notes_events_and_summary(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    initialize_database()

    note = create_note(
        title="Project Notes",
        content="MCP productivity server testing",
    )

    assert note["success"] is True

    notes = search_notes("MCP")

    assert len(notes) == 1
    assert notes[0]["title"] == "Project Notes"

    event = add_event(
        title="Project Review",
        event_date="2026-09-08",
        description="Review MCP project",
    )

    assert event["success"] is True

    events = list_events()

    assert len(events) == 1
    assert events[0]["title"] == "Project Review"

    task = create_task(
        title="Finish MCP testing",
        priority="high",
        due_date="2026-09-08",
    )

    assert task["success"] is True

    summary = daily_summary("2026-09-08")

    assert summary["date"] == "2026-09-08"
    assert summary["task_count"] == 1
    assert summary["event_count"] == 1
    assert summary["pending_tasks"][0]["title"] == "Finish MCP testing"
    assert summary["events"][0]["title"] == "Project Review"
