from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai_assist.agent.chat import ChatAgent


def test_chat_agent(monkeypatch):
    def fake_generate(prompt, model="mistral:instruct"):
        assert "User: hello" in prompt
        return "hi"

    monkeypatch.setattr("ai_assist.agent.chat.generate", fake_generate)
    agent = ChatAgent()
    reply = agent.ask("hello")
    assert reply == "hi"
    # second call includes history
    def fake_generate_hist(prompt, model="mistral:instruct"):
        assert "Assistant: hi" in prompt
        return "bye"

    monkeypatch.setattr("ai_assist.agent.chat.generate", fake_generate_hist)
    assert agent.ask("again") == "bye"
