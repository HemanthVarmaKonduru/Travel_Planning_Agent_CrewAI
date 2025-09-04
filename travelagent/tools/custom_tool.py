from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
import os
import json


class FlightSearchInput(BaseModel):
    """Input schema for flight search."""
    query: str = Field(..., description="Flight search query (e.g., 'flights from NYC to Maldives')")

class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = "Search for flight options, prices, and booking information using web search."
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Error: SERPER_API_KEY not found in environment variables"
        
        url = "https://google.serper.dev/search"
        payload = {
            "q": f"{query} booking prices",
            "num": 8
        }
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get("organic", [])[:5]:
                results.append(f"Title: {item.get('title')}\nURL: {item.get('link')}\nSnippet: {item.get('snippet')}\n")
            
            return "\n".join(results) if results else "No flight results found"
        except Exception as e:
            return f"Error searching for flights: {str(e)}"


class HotelSearchInput(BaseModel):
    """Input schema for hotel search."""
    query: str = Field(..., description="Hotel search query (e.g., 'hotels in Maldives luxury resorts')")

class HotelSearchTool(BaseTool):
    name: str = "Hotel Search Tool"
    description: str = "Search for hotel and accommodation options with pricing and booking information."
    args_schema: Type[BaseModel] = HotelSearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Error: SERPER_API_KEY not found in environment variables"
        
        url = "https://google.serper.dev/search"
        payload = {
            "q": f"{query} booking rates amenities",
            "num": 8
        }
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get("organic", [])[:5]:
                results.append(f"Title: {item.get('title')}\nURL: {item.get('link')}\nSnippet: {item.get('snippet')}\n")
            
            return "\n".join(results) if results else "No hotel results found"
        except Exception as e:
            return f"Error searching for hotels: {str(e)}"


class ActivitySearchInput(BaseModel):
    """Input schema for activity search."""
    query: str = Field(..., description="Activity search query (e.g., 'snorkeling tours Maldives activities')")

class ActivitySearchTool(BaseTool):
    name: str = "Activity Search Tool"
    description: str = "Search for activities, tours, and attractions with pricing and booking information."
    args_schema: Type[BaseModel] = ActivitySearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Error: SERPER_API_KEY not found in environment variables"
        
        url = "https://google.serper.dev/search"
        payload = {
            "q": f"{query} tours booking prices activities",
            "num": 8
        }
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get("organic", [])[:5]:
                results.append(f"Title: {item.get('title')}\nURL: {item.get('link')}\nSnippet: {item.get('snippet')}\n")
            
            return "\n".join(results) if results else "No activity results found"
        except Exception as e:
            return f"Error searching for activities: {str(e)}"


class GeneralSearchInput(BaseModel):
    """Input schema for general search."""
    query: str = Field(..., description="General search query for any travel-related information")

class GeneralSearchTool(BaseTool):
    name: str = "General Search Tool"
    description: str = "General web search for any travel-related information, logistics, or research."
    args_schema: Type[BaseModel] = GeneralSearchInput

    def _run(self, query: str) -> str:
        api_key = os.getenv("SERPER_API_KEY")
        if not api_key:
            return "Error: SERPER_API_KEY not found in environment variables"
        
        url = "https://google.serper.dev/search"
        payload = {
            "q": query,
            "num": 6
        }
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            results = []
            for item in data.get("organic", [])[:4]:
                results.append(f"Title: {item.get('title')}\nURL: {item.get('link')}\nSnippet: {item.get('snippet')}\n")
            
            return "\n".join(results) if results else "No results found"
        except Exception as e:
            return f"Error performing search: {str(e)}"
