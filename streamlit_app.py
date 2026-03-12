"""Streamlit web interface for the Travel Planning Agent."""
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ AI Travel Planning Agent")
st.markdown("*Powered by CrewAI multi-agent framework*")
st.divider()

# Sidebar for API keys
with st.sidebar:
    st.header("🔑 Configuration")
    openai_key = st.text_input(
        "OpenAI API Key",
        type="password",
        value=os.getenv("OPENAI_API_KEY", ""),
        help="Required for LLM-powered agents",
    )
    serper_key = st.text_input(
        "Serper API Key",
        type="password",
        value=os.getenv("SERPER_API_KEY", ""),
        help="Required for web search tools. Get one at serper.dev",
    )

    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key

    st.divider()
    st.markdown("### How it works")
    st.markdown(
        """
        7 specialized AI agents collaborate to plan your trip:
        1. **Clarifier** — validates your requirements
        2. **Flight Researcher** — finds best flights
        3. **Stay Researcher** — compares accommodations
        4. **Activity Planner** — curates daily activities
        5. **Logistics Coordinator** — plans transportation
        6. **Budget Estimator** — optimizes spending
        7. **Synthesis Agent** — compiles final itinerary
        """
    )

# Main form
col1, col2 = st.columns(2)

with col1:
    origin = st.text_input("🛫 Departure City", placeholder="e.g., Dallas, TX")
    start_date = st.date_input("📅 Start Date")
    travelers = st.number_input("👥 Number of Travelers", min_value=1, max_value=20, value=2)
    interests = st.text_area(
        "🎯 Interests",
        placeholder="e.g., temples, beaches, local food, adventure sports",
    )

with col2:
    destination = st.text_input("🛬 Destination", placeholder="e.g., Bali, Indonesia")
    end_date = st.date_input("📅 End Date")
    budget = st.number_input("💰 Total Budget (USD)", min_value=100, max_value=500000, value=5000, step=500)
    preferences = st.text_area(
        "⚙️ Preferences",
        placeholder="e.g., budget-friendly hotels, family activities, vegetarian food",
    )

st.divider()

if st.button("🚀 Plan My Trip", type="primary", use_container_width=True):
    if not openai_key or not serper_key:
        st.error("Please provide both API keys in the sidebar.")
    elif not origin or not destination:
        st.error("Please fill in departure city and destination.")
    else:
        inputs = {
            "origin": origin,
            "destination": destination,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "travelers": str(travelers),
            "budget": str(budget),
            "interests": interests or "sightseeing, local food, culture",
            "preferences": preferences or "mid-range hotels, comfortable travel",
        }

        with st.status("🤖 AI agents are planning your trip...", expanded=True) as status:
            st.write("🔍 Clarifying trip requirements...")
            st.write("✈️ Researching flights...")
            st.write("🏨 Finding accommodations...")
            st.write("🎭 Planning activities...")
            st.write("🚗 Coordinating logistics...")
            st.write("💰 Estimating budget...")
            st.write("📋 Compiling final itinerary...")

            try:
                from travelagent.crew import Travelplanneragent

                result = Travelplanneragent().crew().kickoff(inputs=inputs)
                status.update(label="✅ Trip planned successfully!", state="complete")

                st.balloons()
                st.markdown("## 📋 Your Travel Itinerary")
                st.markdown(str(result))

                # Download button
                st.download_button(
                    label="📥 Download Itinerary (Markdown)",
                    data=str(result),
                    file_name=f"travel_itinerary_{destination.replace(' ', '_')}.md",
                    mime="text/markdown",
                )
            except Exception as e:
                status.update(label="❌ Error occurred", state="error")
                st.error(f"An error occurred: {str(e)}")
                st.info("Make sure your API keys are valid and you have sufficient credits.")

st.divider()
st.caption("Built with CrewAI, OpenAI, and Streamlit")
