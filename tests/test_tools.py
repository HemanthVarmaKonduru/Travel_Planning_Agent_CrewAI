"""Unit tests for custom search tools."""
import os
from unittest.mock import MagicMock, patch

import pytest

from travelagent.tools.custom_tool import (
    ActivitySearchTool,
    FlightSearchTool,
    GeneralSearchTool,
    HotelSearchTool,
    _serper_search,
)


@pytest.fixture
def mock_serper_response():
    """Mock Serper API response."""
    return {
        "organic": [
            {
                "title": "Best Flights to Paris",
                "link": "https://example.com/flights",
                "snippet": "Find cheap flights from NYC to Paris starting at $450.",
            },
            {
                "title": "Cheap Airline Tickets",
                "link": "https://example.com/tickets",
                "snippet": "Compare prices across airlines.",
            },
        ]
    }


class TestSerperSearch:
    """Tests for the core _serper_search helper."""

    def test_missing_api_key(self, monkeypatch):
        monkeypatch.delenv("SERPER_API_KEY", raising=False)
        result = _serper_search("test query")
        assert "SERPER_API_KEY not found" in result

    @patch("travelagent.tools.custom_tool.requests.post")
    def test_successful_search(self, mock_post, mock_serper_response, monkeypatch):
        monkeypatch.setenv("SERPER_API_KEY", "test-key")
        mock_resp = MagicMock()
        mock_resp.json.return_value = mock_serper_response
        mock_resp.raise_for_status.return_value = None
        mock_post.return_value = mock_resp

        result = _serper_search("flights to Paris")
        assert "Best Flights to Paris" in result
        assert "https://example.com/flights" in result

    @patch("travelagent.tools.custom_tool.requests.post")
    def test_empty_results(self, mock_post, monkeypatch):
        monkeypatch.setenv("SERPER_API_KEY", "test-key")
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"organic": []}
        mock_resp.raise_for_status.return_value = None
        mock_post.return_value = mock_resp

        result = _serper_search("obscure query")
        assert "No results found" in result

    @patch("travelagent.tools.custom_tool.requests.post")
    def test_timeout_handling(self, mock_post, monkeypatch):
        import requests as req

        monkeypatch.setenv("SERPER_API_KEY", "test-key")
        mock_post.side_effect = req.exceptions.Timeout("timeout")

        result = _serper_search("test")
        assert "timed out" in result

    @patch("travelagent.tools.custom_tool.requests.post")
    def test_max_items_limit(self, mock_post, monkeypatch):
        monkeypatch.setenv("SERPER_API_KEY", "test-key")
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "organic": [
                {"title": f"Result {i}", "link": f"https://example.com/{i}", "snippet": f"Snippet {i}"}
                for i in range(10)
            ]
        }
        mock_resp.raise_for_status.return_value = None
        mock_post.return_value = mock_resp

        result = _serper_search("test", max_items=3)
        assert result.count("Title:") == 3


class TestToolClasses:
    """Tests for individual tool classes."""

    @patch("travelagent.tools.custom_tool._serper_search")
    def test_flight_search_tool(self, mock_search):
        mock_search.return_value = "Flight results"
        tool = FlightSearchTool()
        result = tool._run("flights NYC to London")
        mock_search.assert_called_once()
        assert "booking prices" in mock_search.call_args[0][0]

    @patch("travelagent.tools.custom_tool._serper_search")
    def test_hotel_search_tool(self, mock_search):
        mock_search.return_value = "Hotel results"
        tool = HotelSearchTool()
        result = tool._run("hotels in London")
        assert "booking rates amenities" in mock_search.call_args[0][0]

    @patch("travelagent.tools.custom_tool._serper_search")
    def test_activity_search_tool(self, mock_search):
        mock_search.return_value = "Activity results"
        tool = ActivitySearchTool()
        result = tool._run("things to do in London")
        assert "tours booking prices activities" in mock_search.call_args[0][0]

    @patch("travelagent.tools.custom_tool._serper_search")
    def test_general_search_tool(self, mock_search):
        mock_search.return_value = "General results"
        tool = GeneralSearchTool()
        result = tool._run("London weather December")
        mock_search.assert_called_once_with("London weather December", num_results=6, max_items=4)
