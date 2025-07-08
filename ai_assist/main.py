"""Main entrypoint for BorisAI."""

from .agent.planner import plan_task


def main():
    """Basic command-line interface."""
    import argparse

    parser = argparse.ArgumentParser(description="Run BorisAI task planner")
    parser.add_argument("prompt", help="Task prompt to plan")
    args = parser.parse_args()

    steps = plan_task(args.prompt)
    for step in steps:
        print(f"- {step}")


if __name__ == "__main__":
    main()
