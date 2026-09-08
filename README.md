# MCP Personal Productivity Server

An AI-powered personal productivity server built with the **Model Context Protocol (MCP)**, **Python**, and **SQLite**.

The server allows AI assistants and agents to manage tasks, save and search notes, track events, and generate daily productivity summaries through structured MCP tools.

## Features

- Create, list, complete, and delete tasks
- Create and search notes
- Add and list events
- Generate daily productivity summaries
- Persistent local storage using SQLite
- MCP-compatible tool interface
- Modular Python architecture

## MCP Tools

The server currently exposes 9 tools:

### Task Management

- `create_task`
- `list_tasks`
- `complete_task`
- `delete_task`

### Notes

- `create_note`
- `search_notes`

### Events

- `add_event`
- `list_events`

### Productivity Summary

- `daily_summary`

## Tech Stack

- Python 3.10+
- Model Context Protocol (MCP)
- MCP Python SDK v2
- SQLite
- Pydantic
- uv
- MCP Inspector

## Project Structure

```text
mcp-personal-productivity-server/
│
├── src/
│   └── productivity_mcp/
│       ├── database/
│       │   ├── __init__.py
│       │   └── db.py
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── events.py
│       │   ├── notes.py
│       │   ├── summary.py
│       │   └── tasks.py
│       │
│       ├── __init__.py
│       └── server.py
│
├── .gitignore
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md