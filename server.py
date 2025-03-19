# server.py
from mcp.server.fastmcp import FastMCP
import yfinance as yf
import pandas as pd

# Create an MCP server
mcp = FastMCP("mcp-yfinance")

@mcp.tool()
async def history(symbol: str) -> pd.DataFrame:
    """
    Get the historical data for a given stock symbol.
    """
    ticker = yf.Ticker(symbol)
    return ticker.history(period="1mo")

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')