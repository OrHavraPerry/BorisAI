from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai_assist.agent.llm import generate


def test_generate_success(monkeypatch):
    class DummyResp:
        def __init__(self, text):
            self.response = text

    def fake_generate(*args, **kwargs):
        return DummyResp("step1\nstep2")

    monkeypatch.setattr("ollama.generate", fake_generate)
    result = generate("do something")
    assert "step1" in result
