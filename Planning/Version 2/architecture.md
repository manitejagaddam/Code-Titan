```bash

                ┌────────────────────┐
                │   User / Prompt    │
                └─────────┬──────────┘
                          │ (specs / request)
                          ▼
                ┌────────────────────┐
                │  Orchestrator      │
                │  (Pipeline Manager)│
                └─────────┬──────────┘
                          │
     ┌────────────────────┼────────────────────┐
     │                    │                    │
     ▼                    ▼                    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ HTML Agent  │     │ CSS Agent   │     │ JS Agent    │
│ (index.html)│     │ (style.css) │     │ (script.js) │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │ (outputs JSON)    │ (outputs JSON)    │ (outputs JSON)
       └───────────────────┼───────────────────┘
                           ▼
                  ┌─────────────────┐
                  │   Critic Agent   │
                  │  (Validation)    │
                  └─────────┬───────┘
                            │
                            ▼
                  ┌─────────────────┐
                  │  File Manager    │
                  │ (Writes files)   │
                  └─────────┬────────┘
                            │
                            ▼
                ┌────────────────────┐
                │   Output Folder     │
                │ index.html          │
                │ style.css           │
                │ script.js           │
                └────────────────────┘

```



⚙️ Components & Responsibilities
1. Orchestrator (Pipeline Manager)

Entry point for the system.

Takes user request/specifications.

Manages flow → HTML → CSS → JS.

Collects agent outputs.

Passes results to Critic → then to File Manager.

2. Agents

HTML Agent → generates index.html.

CSS Agent → styles HTML, outputs style.css.

JS Agent → adds interactivity, outputs script.js.

Each agent returns JSON:

```bash
{
  "filename": "index.html",
  "content": "<!DOCTYPE html>..."
}
```

3. Critic Agent

Reviews generated code:

Validates HTML (structure, W3C rules).

Validates CSS (syntax errors).

Validates JS (basic checks).

If issues found → request fix from the respective agent.

Optional in V2, but critical for scaling.

4. File Manager

Abstracts file writing (no hardcoding).

Handles:

File creation (index.html, style.css, script.js).

Folder organization (e.g., /output/project1/).

Encoding and error handling.

5. Output Folder

Final generated web app:

```bash
/output/
    ├── index.html
    ├── style.css
    └── script.js
```

# 🚀 Workflow Example

## User: “Build me a Todo App.”

- Orchestrator → calls HTML Agent → gets index.html.

- Orchestrator → passes HTML → CSS Agent → gets style.css.

- Orchestrator → passes HTML → JS Agent → gets script.js.

- Orchestrator → sends all to Critic Agent for review.

### Critic returns ✅ → File Manager saves them.

User gets ready-to-run web app.



```bash

multi_agent_webgen/
│
├── agents/
│ ├── html_agent.py
│ ├── css_agent.py
│ ├── js_agent.py
│ └── critic_agent.py
│
├── core/
│ ├── orchestrator.py
│ └── file_manager.py
│
├── output/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── main.py
└── README.md

```