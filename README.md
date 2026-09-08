# 🚀 MCP Personal Productivity Server

> A production-style **Model Context Protocol (MCP) server** that gives AI assistants structured tools to manage tasks, notes, events, and daily productivity workflows.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-MCP-purple)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightblue)
![Tests](https://github.com/Srisahana1/mcp-personal-productivity-server/actions/workflows/tests.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Overview

**MCP Personal Productivity Server** is a Python-based MCP server that demonstrates how AI assistants and agents can interact with persistent productivity data through standardized tools.

Instead of only generating text, an MCP-compatible AI client can use this server to perform actions such as:

- Create and manage tasks
- Store and search notes
- Track scheduled events
- Generate daily productivity summaries
- Persist information locally using SQLite

The project demonstrates practical concepts in **AI agent tooling, Model Context Protocol, structured tool calling, persistent state, modular backend design, automated testing, and CI/CD**.

---

## 🧠 Why This Project?

Modern AI systems are increasingly moving from simple chat interfaces toward **agentic applications** that can interact with external tools and data.

The **Model Context Protocol (MCP)** provides a standardized interface between AI applications and external capabilities.

This project explores that architecture through a real productivity use case:

```text
┌──────────────────────┐
│   AI Assistant /     │
│      MCP Client      │
└──────────┬───────────┘
           │
           │ Model Context Protocol
           ▼
┌──────────────────────┐
│ Personal Productivity│
│      MCP Server      │
├──────────────────────┤
│  9 Structured Tools  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       SQLite         │
│ Persistent Storage   │
└──────────────────────┘
```

---

## ⚡ Key Features

### ✅ Task Management

Create and manage productivity tasks with descriptions, priorities, due dates, and completion status.

### 📝 Notes

Store notes persistently and search them by title or content.

### 📅 Event Management

Create and retrieve scheduled productivity events.

### 📊 Daily Productivity Summary

Generate a consolidated daily view of pending tasks and scheduled events.

### 💾 Persistent Storage

SQLite provides lightweight local persistence, allowing data to remain available across MCP tool calls.

### 🧪 Automated Testing

Core productivity workflows are validated with **pytest**.

### ⚙️ Continuous Integration

**GitHub Actions** automatically runs the test suite whenever code is pushed or a pull request is opened.

---

## 🛠️ MCP Tools

The server currently exposes **9 MCP tools**.

| Tool | Purpose |
|---|---|
| `create_task` | Create a task with priority and due date |
| `list_tasks` | Retrieve active or completed tasks |
| `complete_task` | Mark a task as completed |
| `delete_task` | Delete a task |
| `create_note` | Store a new note |
| `search_notes` | Search saved notes |
| `add_event` | Create an event |
| `list_events` | Retrieve saved events |
| `daily_summary` | Generate a summary of tasks and events for a date |

---

## 🏗️ Architecture

The project separates the MCP interface, business logic, and persistence layer:

```text
MCP Client
    │
    ▼
server.py
    │
    ├── Task Tools
    ├── Note Tools
    ├── Event Tools
    └── Summary Tool
            │
            ▼
     Productivity Logic
            │
            ▼
         SQLite
```

This modular structure makes it easier to extend the server with additional tools, databases, integrations, or AI clients.

---

## 🧰 Tech Stack

| Technology | Usage |
|---|---|
| **Python 3.10+** | Core application |
| **Model Context Protocol** | AI client ↔ tool communication |
| **MCP Python SDK v2** | MCP server implementation |
| **SQLite** | Persistent local storage |
| **Pydantic** | Data validation ecosystem |
| **pytest** | Automated testing |
| **uv** | Dependency/environment management |
| **MCP Inspector** | Interactive MCP tool testing |
| **GitHub Actions** | Continuous integration |

---

## 📂 Project Structure

```text
mcp-personal-productivity-server/
│
├── .github/
│   └── workflows/
│       └── tests.yml
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
├── tests/
│   ├── test_productivity_tools.py
│   └── test_tasks.py
│
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
└── uv.lock
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Srisahana1/mcp-personal-productivity-server.git
cd mcp-personal-productivity-server
```

### 2. Install the project

Using pip:

```bash
pip install -e .
```

Or with uv:

```bash
uv sync
```

### 3. Start the MCP server

```bash
python -m productivity_mcp.server
```

The server runs using MCP's stdio transport and waits for an MCP-compatible client.

---

## 🔍 Test with MCP Inspector

Launch the server using MCP Inspector:

```bash
uv run mcp dev src/productivity_mcp/server.py
```

The Inspector discovers the available MCP tools and allows each tool to be executed interactively.

---

## 💡 Example Workflow

Imagine an AI assistant receives:

> **"Create a high-priority task to prepare for my AI interview tomorrow."**

The MCP client can invoke:

```text
create_task
```

with structured arguments:

```json
{
  "title": "Prepare for AI interview",
  "description": "Review MCP, RAG, and AI agent concepts",
  "priority": "high",
  "due_date": "2026-09-08"
}
```

The task is persisted in SQLite and can later be retrieved through:

```text
list_tasks
```

The assistant can then request:

```text
daily_summary
```

to combine the day's pending tasks and events into one structured response.

---

## 🧪 Testing

Run the automated test suite:

```bash
pytest
```

The tests validate core workflows including:

- Task lifecycle
- Task completion and deletion
- Note creation and search
- Event creation and retrieval
- Daily summary generation
- SQLite persistence

The same test suite runs automatically through **GitHub Actions CI**.

---

## 🗺️ Roadmap

Potential future enhancements include:

- [ ] Update/edit existing tasks
- [ ] Recurring tasks and events
- [ ] Note tags and categories
- [ ] Semantic note search
- [ ] Calendar integration
- [ ] Authentication and multi-user support
- [ ] Cloud database support
- [ ] Productivity analytics
- [ ] Additional MCP resources and prompts
- [ ] Integration with more MCP-compatible AI clients

---

## 🎯 What This Project Demonstrates

This project showcases practical experience with:

**Model Context Protocol • AI Tool Calling • Agentic AI Architecture • Python Backend Development • SQLite • Persistent State • API/Tool Design • Automated Testing • GitHub Actions • CI/CD • Modular Software Architecture**

---

## 📄 License

This project is licensed under the **MIT License**.

---

### ⭐ If you find this project useful, consider starring the repository.
