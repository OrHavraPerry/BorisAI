"""Main entrypoint for BorisAI."""

from .agent.planner import plan_task
from .agent import ChatAgent


def cli(argv: list[str] | None = None) -> None:
    """Command-line interface for BorisAI."""
    import argparse

    parser = argparse.ArgumentParser(description="BorisAI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="Create a numbered plan for a prompt")
    p_plan.add_argument("prompt")
    p_plan.add_argument("--model", default="mistral:instruct")

    p_chat = sub.add_parser("chat", help="Chat with the local model")
    p_chat.add_argument("--model", default="mistral:instruct")

    args = parser.parse_args(argv)

    if args.cmd == "plan":
        try:
            steps = plan_task(args.prompt, model=args.model)
        except Exception as exc:  # LLM or parsing errors
            import sys
            print(f"Error: {exc}", file=sys.stderr)
            raise SystemExit(1)
        for step in steps:
            print(f"- {step}")
    elif args.cmd == "chat":
        agent = ChatAgent(model=args.model)
        print("Type 'exit' to quit.")
        while True:
            try:
                prompt = input("> ")
            except EOFError:
                break
            if prompt.strip().lower() in {"exit", "quit"}:
                break
            try:
                print(agent.ask(prompt))
            except Exception as exc:
                import sys
                print(f"Error: {exc}", file=sys.stderr)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
