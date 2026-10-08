# FastAPI Quick Reference & Workflow Cheatsheet

---

## 1. Daily Workflow

Upon initializing a new terminal session for this project, please proceed with the following steps:

### Step 1: Navigate to the Project Directory
```bash
cd ~/Desktop/fastAPI/"CRASH COURSE"
```

### Step 2: Activate the Virtual Environment
*(This step is required for every new terminal tab if the `(.venv)` prefix is absent from the command prompt)*
```bash
source .venv/bin/activate
```

### Step 3: Execute the Development Server
Select one of the following commands to start the server:

**Option A (Standard Uvicorn command):**
```bash
uvicorn myapi:app --reload
```

**Option B (FastAPI CLI command):**
```bash
fastapi dev myapi.py
```

### Step 4: Terminate the Server / Exit the Virtual Environment
- **Terminate the server:** Press `Ctrl + C`
- **Deactivate the virtual environment:** Execute the command `deactivate`

---

## 2. Browser URLs for API Access

While the server is running (`uvicorn`), you may access your API via the following endpoints:

- **Homepage:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Swagger Interactive API Documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 3. Verifying Your Current Workspace

To ensure you are operating in the correct directory and environment, you may utilize the following commands:

```bash
# Verify the current working directory (Expected output: .../CRASH COURSE):
pwd

# List the directory contents (Ensure myapi.py and .venv are present):
ls

# Verify the visibility of the FastAPI and Pydantic versions within the environment:
python -c "import fastapi, pydantic, uvicorn; print('FastAPI:', fastapi.__version__, '| Pydantic:', pydantic.__version__)"
```

---

## 4. Cheat Sheet: Initializing a New FastAPI Project

Adhere to the following six steps when establishing a new FastAPI project in the future:

```bash
# 1. Create a new directory and navigate into it
mkdir my-project
cd my-project

# 2. Initialize a virtual environment
python -m venv .venv

# 3. Activate the virtual environment
source .venv/bin/activate

# 4. Install FastAPI and standard server dependencies
pip install "fastapi[standard]"

# 5. Prevent editor linting errors (Configure the workspace to reference .venv)
mkdir .vscode
echo '{"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"}' > .vscode/settings.json

# 6. Create the primary executable file
touch main.py
```

---

## 5. Troubleshooting Guide

| Problem / Error | Cause | Resolution |
| :--- | :--- | :--- |
| `error: externally-managed-environment` | The `.venv` was not activated prior to executing the `pip install` command. | Execute `source .venv/bin/activate` before attempting to use `pip`. |
| `Cannot find module 'fastapi'` in the editor | The code editor is referencing the global Python environment instead of the `.venv`. | Press `Ctrl+Shift+P` -> Select `Python: Select Interpreter` -> Choose `./.venv/bin/python`. |
| `bash: cd: python: Not a directory` | The term `python` refers to an executable program/file, not a directory. | Do not use the `cd` command. Execute the program using: `python --version` or `python main.py`. |
| `command not found: uvicorn` | The virtual environment has not been activated in the newly opened terminal. | Execute: `source .venv/bin/activate`. |