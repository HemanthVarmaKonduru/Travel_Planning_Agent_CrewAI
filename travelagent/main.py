#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from travelagent.crew import Travelplanneragent


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'origin': 'Dallas',
        'destination': 'Tirupati',
        'start_date': '2025-12-20',
        'end_date': '2026-01-01',
        'travelers': '4',
        'budget': '15000',
        'interests': 'Visit Temples in India, Beach activities, Good restaurents in Andhra pradesh',
        'preferences': 'budget friendly hotels, Fun activities, Family friendly activities '
    }
    
    try:
        Travelplanneragent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'origin': 'Dallas',
        'destination': 'Hyderabad',
        'start_date': '2025-12-20',
        'end_date': '2026-01-01',
        'travelers': '4',
        'budget': '15000',
        'interests': 'Skydiving, Beach activities, Burj khalifa, fine dining, Dubai Mall, Dubai Aquarium',
        'preferences': 'budget friendly hotels, Fun activities, Family friendly activities '
    }
    try:
        Travelplanneragent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Travelplanneragent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         'origin': 'New York City',
#         'destination': 'Maldives',
#         'start_date': '2024-12-15',
#         'end_date': '2024-12-22',
#         'travelers': '2',
#         'budget': '8000',
#         'interests': 'snorkeling, spa, sunset cruises, fine dining',
#         'preferences': 'overwater villa, adults-only resort, spa services'
#     }
    
#     try:
#         Travelplanneragent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# from .main import run

if __name__ == "__main__":
    run()
