#!/usr/bin/env python
import sys
import warnings
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

from travelagent.crew import Travelplanneragent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def _get_inputs_from_args(args: argparse.Namespace) -> dict:
    """Build crew inputs from CLI arguments."""
    return {
        "origin": args.origin,
        "destination": args.destination,
        "start_date": args.start_date,
        "end_date": args.end_date,
        "travelers": str(args.travelers),
        "budget": str(args.budget),
        "interests": args.interests,
        "preferences": args.preferences,
    }


def _get_default_inputs() -> dict:
    """Default sample inputs for quick testing."""
    return {
        "origin": "Dallas",
        "destination": "Tirupati",
        "start_date": "2025-12-20",
        "end_date": "2026-01-01",
        "travelers": "4",
        "budget": "15000",
        "interests": "Visit Temples in India, Beach activities, Good restaurants in Andhra Pradesh",
        "preferences": "Budget friendly hotels, Fun activities, Family friendly activities",
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="AI-powered Travel Planning Agent using CrewAI"
    )
    sub = parser.add_subparsers(dest="command", help="Available commands")

    # --- run ---
    run_parser = sub.add_parser("run", help="Plan a trip")
    run_parser.add_argument("--origin", default=None, help="Departure city")
    run_parser.add_argument("--destination", default=None, help="Destination city")
    run_parser.add_argument("--start-date", default=None, help="Trip start (YYYY-MM-DD)")
    run_parser.add_argument("--end-date", default=None, help="Trip end (YYYY-MM-DD)")
    run_parser.add_argument("--travelers", type=int, default=None, help="Number of travelers")
    run_parser.add_argument("--budget", type=float, default=None, help="Total budget in USD")
    run_parser.add_argument("--interests", default=None, help="Comma-separated interests")
    run_parser.add_argument("--preferences", default=None, help="Comma-separated preferences")

    # --- train ---
    train_parser = sub.add_parser("train", help="Train the crew")
    train_parser.add_argument("iterations", type=int, help="Number of training iterations")
    train_parser.add_argument("filename", help="Output filename for training data")

    # --- replay ---
    sub.add_parser("replay", help="Replay a specific task").add_argument(
        "task_id", help="Task ID to replay"
    )

    return parser


def run(inputs: dict | None = None) -> None:
    """Run the travel planning crew."""
    inputs = inputs or _get_default_inputs()

    required = ["origin", "destination", "start_date", "end_date", "travelers", "budget"]
    missing = [k for k in required if not inputs.get(k)]
    if missing:
        raise ValueError(f"Missing required inputs: {', '.join(missing)}")

    print(f"\nPlanning trip: {inputs['origin']} -> {inputs['destination']}")
    print(f"Dates: {inputs['start_date']} to {inputs['end_date']}")
    print(f"Travelers: {inputs['travelers']} | Budget: ${inputs['budget']}\n")

    Travelplanneragent().crew().kickoff(inputs=inputs)


def train(n_iterations: int, filename: str) -> None:
    """Train the crew for a given number of iterations."""
    inputs = _get_default_inputs()
    Travelplanneragent().crew().train(
        n_iterations=n_iterations, filename=filename, inputs=inputs
    )


def replay(task_id: str) -> None:
    """Replay the crew execution from a specific task."""
    Travelplanneragent().crew().replay(task_id=task_id)


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    if not args.command:
        # No subcommand — run with defaults
        run()
        return

    if args.command == "run":
        if args.origin:
            inputs = _get_inputs_from_args(args)
        else:
            inputs = _get_default_inputs()
        run(inputs)
    elif args.command == "train":
        train(args.iterations, args.filename)
    elif args.command == "replay":
        replay(args.task_id)


if __name__ == "__main__":
    main()
