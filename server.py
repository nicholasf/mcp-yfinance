# server.py
from mcp.server.fastmcp import FastMCP
import yfinance as yf
import pandas as pd

# Create an MCP server
mcp = FastMCP("mcp-yfinance")

@mcp.tool()
async def history(symbol: str, **kwargs) -> pd.DataFrame:
    """
    Get the historical data for a given stock symbol.
    """
    ticker = yf.Ticker(symbol)
    return ticker.history(**kwargs)

@mcp.tool()
async def latest(symbol: str) -> float:
    """
    Get the latest stock price for a given symbol.
    """
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="1d")
    return df["Close"].iloc[-1]

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')