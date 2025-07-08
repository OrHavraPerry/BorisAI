from pathlib import Path
import sys
import importlib

sys.path.append(str(Path(__file__).resolve().parents[1]))

main_mod = importlib.import_module("ai_assist.main")


def test_cli_plan(monkeypatch, capsys):
    def fake_plan(prompt, model="mistral:instruct"):
        assert prompt == "test"
        return ["step1", "step2"]

    monkeypatch.setattr(main_mod, "plan_task", fake_plan)
    main_mod.cli(["plan", "test"])
    captured = capsys.readouterr()
    assert "step1" in captured.out
    assert "step2" in captured.out
