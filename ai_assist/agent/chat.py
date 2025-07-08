"""Simple chat agent for BorisAI."""

from ..memory import Memory
from .llm import generate


class ChatAgent:
    """Minimal conversational agent using the local LLM."""

    def __init__(self, model: str = "mistral:instruct") -> None:
        self.model = model
        self.memory = Memory()

    def ask(self, message: str) -> str:
        """Return the LLM response and store conversation history."""
        history = "\n".join(self.memory.get_all())
        prompt = f"{history}\nUser: {message}\nAssistant:" if history else f"User: {message}\nAssistant:"
        reply = generate(prompt, model=self.model).strip()
        self.memory.add(f"User: {message}")
        self.memory.add(f"Assistant: {reply}")
        return reply
