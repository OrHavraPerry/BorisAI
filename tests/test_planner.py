from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai_assist.agent import plan_task


def test_plan_task(monkeypatch):
    def fake_generate(prompt, model="mistral:instruct"):
        return "1. step1\n2. step2"

    monkeypatch.setattr("ai_assist.agent.planner.generate", fake_generate)
    steps = plan_task("test")
    assert steps == ["step1", "step2"]
