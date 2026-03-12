# ✈️ AI Travel Planning Agent — CrewAI Multi-Agent System

An intelligent travel planning system that orchestrates **7 specialized AI agents** to collaboratively build comprehensive, personalized travel itineraries — from flights and hotels to daily activities and budget optimization.

Built with [CrewAI](https://crewai.com), [OpenAI](https://openai.com), and [Serper](https://serper.dev) for real-time web search.

## 🎯 What It Does

Give it a destination, dates, and budget — and the agents handle everything:

| Agent | Role |
|-------|------|
| **Clarifier** | Validates and structures your travel requirements |
| **Flight Researcher** | Finds optimal routes, airlines, and booking links |
| **Stay Researcher** | Compares hotels/resorts matching your preferences |
| **Activity Planner** | Curates day-by-day experiences aligned with your interests |
| **Logistics Coordinator** | Plans transfers, local transport, and timing |
| **Budget Estimator** | Tracks spending and suggests cost optimizations |
| **Synthesis Agent** | Compiles everything into a polished Markdown itinerary |

## 🏗️ Architecture

```
User Input → Clarifier Agent → Flight Agent → Stay Agent → Activity Agent
                                                                    ↓
              Final Itinerary ← Synthesis Agent ← Budget Agent ← Logistics Agent
```

All agents execute sequentially, each building on previous outputs. The system uses Serper API for real-time web searches to ground recommendations in current data.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- OpenAI API key ([get one](https://platform.openai.com/api-keys))
- Serper API key ([get one](https://serper.dev))

### Setup

```bash
# Clone the repo
git clone https://github.com/hemanthvarmakonduru/Travel_Planning_Agent_CrewAI.git
cd Travel_Planning_Agent_CrewAI

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your API keys
```

### Run via CLI

```bash
# Quick run with default inputs
python -m travelagent.main

# Custom trip
python -m travelagent.main run \
  --origin "New York" \
  --destination "Tokyo" \
  --start-date 2025-04-01 \
  --end-date 2025-04-10 \
  --travelers 2 \
  --budget 8000 \
  --interests "temples, sushi, anime, cherry blossoms" \
  --preferences "mid-range hotels, public transit"
```

### Run via Web UI (Streamlit)

```bash
streamlit run streamlit_app.py
```

Opens an interactive web interface where you can fill in trip details and get your itinerary with a single click.

## 📂 Project Structure

```
├── travelagent/
│   ├── main.py              # CLI entry point with argument parsing
│   ├── crew.py              # CrewAI agent & task definitions
│   ├── config/
│   │   ├── agents.yaml      # Agent roles, goals, and backstories
│   │   └── tasks.yaml       # Task descriptions and expected outputs
│   └── tools/
│       └── custom_tool.py   # Serper-powered search tools
├── tests/
│   ├── test_tools.py        # Tool unit tests with mocked APIs
│   └── test_main.py         # Input validation tests
├── streamlit_app.py          # Web UI
├── .github/workflows/ci.yml  # CI pipeline
├── .env.example              # Environment template
├── requirements.txt
└── LICENSE
```

## 🧪 Testing

```bash
pytest tests/ -v
```

## 📄 Sample Output

The agent generates a detailed Markdown itinerary including:
- Flight options with booking links and price comparisons
- Hotel recommendations with amenities and ratings
- Day-by-day activity schedule with timing and costs
- Transportation logistics and transfer details
- Complete budget breakdown with optimization tips
- Booking checklist with priority deadlines

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | CrewAI |
| LLM | OpenAI GPT-4o |
| Web Search | Serper API |
| Web UI | Streamlit |
| Testing | pytest |
| CI/CD | GitHub Actions |

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.
