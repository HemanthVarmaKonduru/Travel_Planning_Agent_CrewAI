# ✈️ Travel Planning Agent with CrewAI: A Comprehensive Guide

This document provides a detailed overview of the Travel Planning Agent project, built using CrewAI. It outlines the project structure, key components, and their functionalities, offering a comprehensive guide to understanding and utilizing the agent for automated travel planning.

## 📁 Project Structure

The project is organized into several key directories and files:

```
TravelPlanningAgent_CrewAI/                     # The root directory of the project
├── Travel_Planning_Agent_CrewAI/               # Contains the core application logic
│   ├── travelagent/                            # The main application directory
│   │   ├── knowledge/                          # Stores persistent knowledge
│   │   │   └── user_preference.txt             # Stores user preferences for personalized travel planning
│   │   ├── src/                                # Contains the source code
│   │   │   ├── requirements.txt                # Lists the Python dependencies required to run the project
│   │   │   ├── travel_itinerary.md             # The generated travel itinerary output file
│   │   │   └── travelagent/                    # Contains the Python modules
│   │   │       ├── __init__.py                 # Initializes the travelagent package
│   │   │       ├── main.py                     # The application entry point
│   │   │       ├── crew.py                     # Defines the crew and agent configurations
│   │   │       ├── config/                     # Contains configuration files
│   │   │       │   ├── agents.yaml             # Defines the configurations for each agent
│   │   │       │   └── tasks.yaml              # Defines the tasks to be performed by agents
│   │   │       └── tools/                      # Contains custom tools
│   │   │           ├── __init__.py             # Initializes the tools package
│   │   │           └── custom_tool.py          # Implements custom search tools
│   │   ├── tests/                              # Contains test files for validating functionality
│   │   ├── pyproject.toml                      # Specifies project metadata and dependencies
│   │   └── README.md                           # Project description and usage instructions
│   └── TravelAgentEnv/                         # Virtual environment for the project
```

## 🔧 Key Components

### 1. **user_preference.txt**

This file stores user-specific travel preferences, allowing the agent to personalize the travel itinerary based on individual needs and desires. Examples of preferences include:

- **Destination preferences** (e.g., specific cities, countries, or types of locations like beaches or mountains)
- **Budget constraints**
- **Travel dates and duration**
- **Preferred mode of transportation** (e.g., flights, trains, cars)
- **Accommodation preferences** (e.g., hotels, hostels, Airbnb)
- **Activity preferences** (e.g., sightseeing, adventure, relaxation)
- **Dietary restrictions or allergies**
- **Interests** (e.g., history, art, music)

### 2. **requirements.txt**

This file lists all the Python packages required to run the Travel Planning Agent. Using a requirements.txt file ensures that the project can be easily set up and run on different machines by installing the specified dependencies. Example dependencies include:

- **crewai**: The core CrewAI library for building autonomous agents
- **openai**: The OpenAI Python library for interacting with OpenAI models
- **requests**: A library for making HTTP requests to external APIs
- **beautifulsoup4**: A library for parsing HTML and XML documents
- **python-dotenv**: A library for loading environment variables from a .env file

### 3. **travel_itinerary.md**

This file is the output of the Travel Planning Agent. It contains the generated travel itinerary in Markdown format, making it easily readable and editable. The itinerary typically includes:

- **Destination(s)**
- **Travel dates**
- **Transportation details** (e.g., flight numbers, train schedules)
- **Accommodation details** (e.g., hotel names, addresses, booking confirmations)
- **Planned activities and attractions**
- **Estimated costs**
- **Useful links and resources**

### 4. **main.py**

This is the main entry point of the application. It orchestrates the entire travel planning process by performing the following actions:

- **Loads configurations** from `agents.yaml` and `tasks.yaml`
- **Initializes the CrewAI agents** based on the configurations
- **Assigns tasks** to the agents
- **Runs the crew** to execute the tasks
- **Collects the results** from the agents
- **Formats the results** into a travel itinerary
- **Writes the itinerary** to `travel_itinerary.md`

### 5. **crew.py**

This file defines the crew and agent configurations. It specifies the roles, goals, and tools of each agent in the crew. For example, a crew might consist of the following agents:

- **Travel Researcher**: Responsible for researching potential destinations, attractions, and activities
- **Flight Booker**: Responsible for finding and booking flights
- **Accommodation Booker**: Responsible for finding and booking hotels or other accommodations
- **Itinerary Planner**: Responsible for creating a detailed travel itinerary based on the research and bookings

### 6. **agents.yaml**

This file contains the configuration details for each agent. It defines the agent's:

- **Role**: A descriptive name for the agent's function (e.g., "Travel Researcher")
- **Goal**: The agent's objective (e.g., "Research potential destinations based on user preferences")
- **Backstory**: A brief description of the agent's background and expertise
- **Tools**: A list of tools that the agent can use to accomplish its tasks
- **Memory**: Whether the agent should retain information from previous interactions
- **LLM (Language Model)**: Specifies the language model to be used by the agent (e.g., GPT-3.5, GPT-4)

### 7. **tasks.yaml**

This file defines the tasks to be performed by the agents. It specifies the:

- **Description**: A detailed description of the task
- **Agent**: The agent assigned to perform the task
- **Context**: Any relevant context or information needed to complete the task

### 8. **custom_tool.py**

This file implements custom search tools for retrieving travel-related information. These tools can be used to access external APIs or websites to gather data on flights, hotels, attractions, and other travel-related services. Examples of custom tools include:

- **Flight Search Tool**: Uses an API to search for flights based on origin, destination, dates, and budget
- **Hotel Search Tool**: Uses an API to search for hotels based on location, dates, and budget
- **Attraction Search Tool**: Uses an API or web scraping to find information about attractions in a specific location

## 🔄 Workflow

The Travel Planning Agent operates as follows:

1. **Configuration Loading**: The `main.py` script loads the agent and task configurations from `agents.yaml` and `tasks.yaml`

2. **Agent Initialization**: The script initializes the CrewAI agents based on the configurations

3. **Task Assignment**: The script assigns tasks to the agents

4. **Task Execution**: The CrewAI framework orchestrates the execution of the tasks by the agents

5. **Information Gathering**: Each agent uses its assigned tools to gather information and perform its assigned tasks

6. **Agent Collaboration**: The agents communicate and collaborate to achieve the overall goal of creating a travel itinerary

7. **Result Collection**: The `main.py` script collects the results from the agents and formats them into a travel itinerary

8. **Output Generation**: The script writes the itinerary to the `travel_itinerary.md` file

## 🚀 Usage

To use the Travel Planning Agent:

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Agents and Tasks**
   - Configure the agents and tasks in `agents.yaml` and `tasks.yaml` according to your needs

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **View Results**
   - The generated travel itinerary will be saved in `travel_itinerary.md`

## 📋 Summary

This comprehensive guide provides a detailed overview of the Travel Planning Agent project, its structure, key components, and functionalities. By understanding these elements, users can effectively utilize and customize the agent for automated travel planning.

### Key Benefits
- **Automated Planning**: Streamlines the entire travel planning process
- **Personalization**: Adapts to individual user preferences and requirements
- **Comprehensive Coverage**: Handles all aspects from flights to activities
- **Extensible Design**: Easy to add new agents and customize functionality
- **Professional Output**: Generates well-formatted, detailed itineraries

---

*Built with ❤️ using CrewAI Framework*
