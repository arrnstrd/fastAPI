
```markdown
# FastAPI Quick Reference & Workflow Cheatsheet

---

## 1. Pang Araw-araw na Workflow (Daily Workflow)

Tuwing magbubukas ka ng bagong terminal session sa project na ito:

### Step 1: Pumunta sa Project Directory
```bash
cd ~/Desktop/fastAPI/"CRASH COURSE"
```

### Step 2: I-activate ang Virtual Environment
*(Kailangan ito sa bawat bagong terminal tab kung walang `(.venv)` sa prompt)*
```bash
source .venv/bin/activate
```

### Step 3: Patakbuhin ang Development Server
Pumili ng isa sa dalawang commands:

**Option A (Standard Uvicorn command):**
```bash
uvicorn myapi:app --reload
```

**Option B (FastAPI CLI command):**
```bash
fastapi dev myapi.py
```

### Step 4: Patayin ang Server / Lumabas sa Venv
- **Itigil ang server:** Pindutin ang `Ctrl + C`
- **I-deactivate ang venv:** I-type ang `deactivate`

---

## 2. Browser URLs para Makita ang API Mo

Kapag tumatakbo ang server (`uvicorn`):

- **Homepage:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Swagger Interactive API Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 3. Paano I-check Kung Nasa Tamang Lugar Ka

```bash
# Tingnan ang current directory (Dapat: .../CRASH COURSE):
pwd

# Tingnan ang mga files (Dapat nakikita mo ang myapi.py at .venv):
ls

# I-test kung nakikita ang FastAPI at Pydantic versions:
python -c "import fastapi, pydantic, uvicorn; print('FastAPI:', fastapi.__version__, '| Pydantic:', pydantic.__version__)"
```

---

## 4. Cheat Sheet: Paggawa ng Bagong FastAPI Project Mula sa Simula

Sundin itong 6 na steps tuwing may bago kang gagawing project sa future:

```bash
# 1. Gawa ng folder at pumasok sa loob
mkdir aking-proyekto
cd aking-proyekto

# 2. Gumawa ng virtual environment
python -m venv .venv

# 3. I-activate ito
source .venv/bin/activate

# 4. I-install ang FastAPI + Server tools
pip install "fastapi[standard]"

# 5. Pigilan ang editor red-line errors (Config para ituro sa .venv)
mkdir .vscode
echo '{"python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"}' > .vscode/settings.json

# 6. Gumawa ng main file
touch main.py
```

---

## 5. Quick Troubleshooting

| Problema / Error | Dahilan | Solusyon |
| :--- | :--- | :--- |
| `error: externally-managed-environment` | Hindi activated ang `.venv` bago nag-`pip install`. | Patakbuhin: `source .venv/bin/activate` bago mag-pip. |
| `Cannot find module 'fastapi'` sa editor | Nakatingin ang editor sa Global Python imbes na sa `.venv`. | Pindutin ang `Ctrl+Shift+P` -> `Python: Select Interpreter` -> Piliin ang `./.venv/bin/python`. |
| `bash: cd: python: Not a directory` | Ang `python` ay isang executable program/file, hindi folder. | Huwag i-cd. Patakbuhin ito gamit ang: `python --version` o `python main.py`. |
| `command not found: uvicorn` | Hindi activated ang virtual environment sa bagong bukas na terminal. | I-type: `source .venv/bin/activate`. |
```