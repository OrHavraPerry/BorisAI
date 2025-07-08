"""Basic LLM interface for BorisAI using the official Ollama client."""

import ollama


def generate(prompt: str, model: str = "mistral:instruct") -> str:
    """Return a completion from the local Ollama server."""
    try:
        resp = ollama.generate(model=model, prompt=prompt, stream=False)
        return resp["response"] if isinstance(resp, dict) else resp.response
    except Exception as exc:  # network errors or missing server
        raise RuntimeError(f"LLM request failed: {exc}") from exc
