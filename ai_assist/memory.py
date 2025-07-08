"""Simple in-memory storage placeholder."""


class Memory:
    """Store conversation history for now."""

    def __init__(self):
        self._messages = []

    def add(self, message: str) -> None:
        self._messages.append(message)

    def get_all(self):
        return list(self._messages)
