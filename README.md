# 🤖 AI Personal Assistant

A professional **AI Personal Assistant** built with **Python, Streamlit, OpenAI Agents SDK, and Google Gemini**.

The assistant uses a **multi-agent architecture** where different specialized agents handle different types of tasks such as mathematics, coding, research, memory, tasks, time, and file management.

---

## ✨ Features

- 🤖 AI Personal Assistant
- 🧠 Conversation memory
- 💾 Long-term personal memory
- 🧮 Mathematical calculations
- ✅ Task creation and management
- 💻 Coding assistance
- 🔎 Research planning
- 🕐 Current date and time
- 📁 Project file exploration
- 📝 Notes management
- 🔀 Multi-agent handoffs
- 🛠️ Agents as tools
- 🛡️ Input and output guardrails
- 📊 Custom activity logging
- 🧪 Evaluation system
- 🎨 Professional Streamlit UI
- 🌙 Modern dark dashboard
- 🔐 Environment-based API key management

---

## 🏗️ Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │   Streamlit UI  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Main Assistant │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Math Agent    Task Agent    Memory Agent
             │             │             │
             ├─────────────┼─────────────┤
             │             │             │
             ▼             ▼             ▼
       Coding Agent   Research Agent  Time Agent
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                      File Agent
                           │
                           ▼
                    Gemini 2.5 Flash
