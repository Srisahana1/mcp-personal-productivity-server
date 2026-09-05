"""MCP Personal Productivity Server."""

from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Personal Productivity Server")


@mcp.tool()
def hello(name: str) -> str:
    """Return a welcome message to verify that the MCP server is working."""
    return f"Hello, {name}! Your Personal Productivity MCP Server is running."


if __name__ == "__main__":
    mcp.run()
