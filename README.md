✈️ **Travel Planning Agent with CrewAI**

This project features a Travel Planning Agent built with the CrewAI framework. It's designed to streamline the travel planning process by using a crew of specialized AI agents. Each agent has a specific role, working collaboratively to create a comprehensive and personalized travel itinerary, complete with flight details, accommodations, activities, and a budget breakdown.

💡 Project Explanation
The core of this project is its modular design. By breaking down the complex task of travel planning into specialized roles, the system can handle detailed requests with greater accuracy and efficiency.

<img width="1779" height="1278" alt="Image" src="https://github.com/user-attachments/assets/3792183a-8632-4a95-bcd9-50f2e3535a53" />



**Key Components**
Agents: Each agent is a specialized AI with a clearly defined purpose:
Clarifier Agent: Ensures all user inputs are precise and complete.
Flight Research Agent: Focuses exclusively on finding the best flight options.
Stay Research Agent: Handles all aspects of finding and shortlisting accommodations.
Activity Planner Agent: Curates a list of engaging daily activities based on interests.
Logistics Agent: Manages the practical, on-the-ground details of the trip.
Budget Estimator Agent: Calculates and manages the financial aspects of the trip.
Synthesis Agent: Compiles all the information into a final, user-friendly itinerary.

**Tasks**: These are the specific jobs assigned to each agent. The tasks are designed to create a logical, step-by-step workflow:
Clarify trip requirements.
Research flights.
Research accommodations.
Plan daily activities.
Coordinate logistics.
Estimate the total budget.
Compile the final itinerary.

**Custom Tools**: Agents use custom-built tools to interact with real-world data sources. Examples include FlightSearchTool, HotelSearchTool, ActivitySearchTool, and GeneralSearchTool to perform targeted searches.

<p class="demoTitle">&nbsp;</p>
<p>&nbsp;TravelPlanningAgent_CrewAI/</p>
<div>
<div>├── Travel_Planning_Agent_CrewAI/</div>
<div>│ ├── travelagent/</div>
<div>│ │ ├── knowledge/</div>
<div>│ │ │ └── user_preference.txt # User preference storage</div>
<div>│ │ ├── src/</div>
<div>│ │ │ ├── requirements.txt # Python dependencies</div>
<div>│ │ │ ├── travel_itinerary.md # Generated itinerary output</div>
<div>│ │ │ └── travelagent/</div>
<div>│ │ │ ├── __init__.py</div>
<div>│ │ │ ├── main.py # Application entry point</div>
<div>│ │ │ ├── crew.py # Crew and agent definitions</div>
<div>│ │ │ ├── config/</div>
<div>│ │ │ │ ├── agents.yaml # Agent configurations</div>
<div>│ │ │ │ └── tasks.yaml # Task definitions</div>
<div>│ │ │ └── tools/</div>
<div>│ │ │ ├── __init__.py</div>
<div>│ │ │ └── custom_tool.py # Custom search tools</div>
<div>│ │ ├── tests/ # Test files</div>
<div>│ │ ├── pyproject.toml # Project configuration</div>
<div>│ │ └── README.md # This file</div>
<div>│ └── TravelAgentEnv/ # Virtual environment</div>
<div>```</div>
</div>




🔑 **Environment Variables**
The project requires specific API keys to function. These should be stored in a .env file located in the src directory.

Example .env file:
Code snippet

MODEL="your_model_name_here"
OPENAI_API_KEY="your_openai_api_key_here"
SERPER_API_KEY="your_serper_api_key_here"


🚀 Installation
Clone the repository:

Bash
git clone <repository-url>
cd TravelPlanningAgent_CrewAI
Create and activate a virtual environment:

Bash
python3 -m venv TravelAgentEnv
source TravelAgentEnv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the src directory.

Add your required API keys as shown in the example above.

▶️ Usage
Navigate to the src directory:

Bash
cd travelagent/src
Run the main script:

Bash
python -m travelagent.main
To test different scenarios, you can customize the inputs dictionary directly in the main.py file.

🛠️ **Configuration**
Agents: The behavior and expertise of each agent are defined in config/agents.yaml.
Tasks: The sequential workflow is outlined in config/tasks.yaml.
