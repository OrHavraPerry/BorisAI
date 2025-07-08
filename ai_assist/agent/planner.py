"""Simple task planner stub."""

from typing import List


def plan_task(prompt: str) -> List[str]:
    """Return a list of steps for the given prompt.

    This is a placeholder that just echoes the prompt.
    """
    # In the future this will call a language model.
    return [f"Plan for: {prompt}"]
