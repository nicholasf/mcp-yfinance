A simple wrapper around the classic [yFinance](https://github.com/ranaroussi/yfinance) that operates as an MCP tool.

## Install

Register it as an extension in your MCP host.

On [goose](https://github.com/block/goose):

```

☁  mcp-yfinance [main] ⚡  goose configure    

This will update your existing config file
  if you prefer, you can edit it directly at /home/nicholasf/.config/goose/config.yaml

┌   goose-configure 
│
◇  What would you like to configure?
│  Add Extension 
│
◇  What type of extension would you like to add?
│  Command-line Extension 
│
◇  What would you like to call this extension?
│  yf
│
◇  What command should be run?
│  uv run server.py
│
◇  Please set the timeout for this tool (in secs):
│  5
│
◇  Would you like to add environment variables?
│  No 
│
└  Added yf extension

```


Then invoke it:

```
☁  mcp-yfinance [main] ⚡  goose session -n yf
starting session | provider: anthropic model: claude-3-5-sonnet-latest
    logging to /home/nicholasf/.local/share/goose/sessions/yf.jsonl
    working directory: /home/nicholasf/code/github/nicholasf/mcp-yfinance

Goose is running! Enter your instructions, or try asking what goose can do.

( O)> yf__history AAPL
I'll try getting Apple's stock history now.
─── history | yf ──────────────────────────
symbol: AAPL



Great! The command is now working correctly. The data shows Apple's stock performance over the last month (from February 19, 2025 to March 18, 2025). Here are some key observations:

1. The stock has shown a general downward trend over this period
2. Starting price (Feb 19): Around $244.66
3. Latest price (March 18): Around $214.16
4. Highest point: Around $250.00 (Feb 25)
5. Notable decline: A sharp drop occurred around March 11, falling from ~$235 to ~$223

The data includes Open, High, Low, Close prices, Volume, Dividends, and Stock Splits (though no dividends or splits occurred during this period).

Would you like to:
1. See the data for a different time period?
2. Look at a different stock symbol?
3. Get more detailed analysis of specific aspects of this data?

Just let me know what information would be most helpful!


```