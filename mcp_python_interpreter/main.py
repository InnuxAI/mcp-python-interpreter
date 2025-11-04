"""Main module for mcp-python-interpreter."""

from mcp_python_interpreter.server import mcp


def main():
    """Run the MCP Python Interpreter server."""
    mcp.run(transport='streamable-http')


if __name__ == "__main__":
    main()
