"""Simple task planner."""

from typing import List

from .llm import generate


def plan_task(prompt: str, *, model: str = "mistral:instruct") -> List[str]:
    """Return a list of steps for the given prompt using the local LLM."""
    response = generate(
        f"Create a short numbered list of steps to accomplish: {prompt}",
        model=model,
    )
    steps = []
    for line in response.splitlines():
        line = line.strip()
        if not line:
            continue
        line = line.lstrip("-0123456789. ")
        steps.append(line)
    return steps
