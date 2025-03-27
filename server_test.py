import pytest
from server import history
from unittest.mock import MagicMock

@pytest.fixture
def mock_yf_ticker(monkeypatch):
    mock_ticker = MagicMock()
    mock_history = MagicMock()
    mock_ticker.history = mock_history
    monkeypatch.setattr("server.yf.Ticker", lambda symbol: mock_ticker)
    return mock_ticker, mock_history

@pytest.mark.asyncio
async def test_history_calls_ticker_history(mock_yf_ticker):
    _, mock_history = mock_yf_ticker
    mock_history.return_value = "mocked_data"
    
    result = await history("AAPL", period="1d", interval="1m")
    
    mock_history.assert_called_once_with(period="1d", interval="1m")
    assert result == "mocked_data"

@pytest.mark.asyncio
async def test_history_passes_kwargs_to_ticker_history(mock_yf_ticker):
    mock_ticker, mock_history = mock_yf_ticker
    mock_history.return_value = "mocked_data"

    kwargs = {"period": "5d", "interval": "15m", "prepost": True}
    result = await history("AAPL", **kwargs)

    mock_ticker.history.assert_called_once_with(**kwargs)
    assert result == "mocked_data"
