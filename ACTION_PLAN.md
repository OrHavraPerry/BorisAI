# Action Plan

Below is a high-level checklist derived from `plan.md` to bootstrap the project.

1. **Set up the Python environment**
   - Create a virtual environment: `python -m venv ai-assist`
   - Install core packages: `pip install --upgrade pip`

2. **Install the local model runner**
   - Install [Ollama](https://ollama.com) and pull a small model, e.g. `mistral:instruct`.

3. **Install required Python packages**
   - Examples: `autogen`, `crewai`, `langgraph`, `open-interpreter`, `chromadb`, `pyautogui`, `playwright`, `faster-whisper`, `pdfplumber`, `pynput`.
   - Run `playwright install chromium` to enable browser automation.

4. **Create the project skeleton**
   - `ai_assist/`
     - `main.py` – entrypoint
     - `agent/` with `planner.py`, `memory.py`, and `tools/`
     - `ui/` for tray or voice interfaces

5. **Implement a few core tools**
   - File operations (find, move, etc.)
   - Basic system app launching
   - Browser automation

6. **Integrate with an agent framework**
   - Use AutoGen or an alternative to plan tasks and call your tools.

7. **Add optional extras**
   - Voice or hotkey listener for quick commands
   - Memory storage with ChromaDB

8. **Guardrails**
   - Allow‑lists for destructive actions
   - Step counter to avoid infinite loops

9. **Smoke tests**
   - Organize screenshots
   - Summarize a PDF
   - Launch a desktop app and control it

10. **Future work**
   - GUI (Electron or Tauri)
   - Schedulers or IoT hooks
   - Fine tuning small models with your data

Refer to `plan.md` for detailed explanations and rationale behind each step.
