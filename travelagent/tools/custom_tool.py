import logging
import os
from typing import Type

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

SERPER_API_URL = "https://google.serper.dev/search"
REQUEST_TIMEOUT = 15


def _serper_search(query: str, num_results: int = 8, max_items: int = 5) -> str:
    """Execute a search query using the Serper API with error handling."""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return "Error: SERPER_API_KEY not found. Set it in your .env file."

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }
    payload = {"q": query, "num": num_results}

    try:
        response = requests.post(
            SERPER_API_URL,
            json=payload,
            headers=headers,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        results = []
        for item in data.get("organic", [])[:max_items]:
            results.append(
                f"Title: {item.get('title')}\n"
                f"URL: {item.get('link')}\n"
                f"Snippet: {item.get('snippet')}\n"
            )
        return "\n".join(results) if results else "No results found."
    except requests.exceptions.Timeout:
        logger.warning("Serper API request timed out for query: %s", query)
        return "Error: Search request timed out. Please try again."
    except requests.exceptions.HTTPError as e:
        logger.error("Serper API HTTP error: %s", e)
        return f"Error: Search API returned status {e.response.status_code}."
    except Exception as e:
        logger.error("Unexpected error during search: %s", e)
        return f"Error performing search: {str(e)}"


# --- Input Schemas ---

class FlightSearchInput(BaseModel):
    """Input schema for flight search."""
    query: str = Field(..., description="Flight search query (e.g., 'flights from NYC to Maldives December 2025')")


class HotelSearchInput(BaseModel):
    """Input schema for hotel search."""
    query: str = Field(..., description="Hotel search query (e.g., 'luxury resorts in Maldives with pool')")


class ActivitySearchInput(BaseModel):
    """Input schema for activity search."""
    query: str = Field(..., description="Activity search query (e.g., 'snorkeling tours in Maldives')")


class GeneralSearchInput(BaseModel):
    """Input schema for general search."""
    query: str = Field(..., description="General search query for any travel-related information")


# --- Tools ---

class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = "Search for flight options, prices, and booking information using web search."
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, query: str) -> str:
        return _serper_search(f"{query} booking prices", num_results=8, max_items=5)


class HotelSearchTool(BaseTool):
    name: str = "Hotel Search Tool"
    description: str = "Search for hotel and accommodation options with pricing and booking information."
    args_schema: Type[BaseModel] = HotelSearchInput

    def _run(self, query: str) -> str:
        return _serper_search(f"{query} booking rates amenities", num_results=8, max_items=5)


class ActivitySearchTool(BaseTool):
    name: str = "Activity Search Tool"
    description: str = "Search for activities, tours, and attractions with pricing and booking information."
    args_schema: Type[BaseModel] = ActivitySearchInput

    def _run(self, query: str) -> str:
        return _serper_search(f"{query} tours booking prices activities", num_results=8, max_items=5)


class GeneralSearchTool(BaseTool):
    name: str = "General Search Tool"
    description: str = "General web search for any travel-related information, logistics, or research."
    args_schema: Type[BaseModel] = GeneralSearchInput

    def _run(self, query: str) -> str:
        return _serper_search(query, num_results=6, max_items=4)
