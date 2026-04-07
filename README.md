# ✨ QuickNote AI

Smart notebook with auto-tagging, AI-powered insights, and contextual search.

---

## 🎬 Demo

### Interface Screenshots

#### Main Page
![Main](screenshots/write_note.png)
*Note input, save button, results area*

#### Smart Search
![Search](screenshots/smart_search.png)
*Contextual answer to query across notes*

#### Notes History
![History](screenshots/store.png)
*Expandable cards with full content*

---

## 🌍 Product Context

### Target Users
- Students taking lecture and lab notes
- Developers capturing ideas and tasks
- Anyone who takes notes and wants to find them quickly

### Problem Solved for End Users
1. **Notes get lost**: Manual saving across different places, no unified storage
2. **Search doesn't work**: Hard to find notes by keywords, especially if you forget exact wording
3. **No automation**: Manual tagging takes time, easy to forget categorization
4. **No intelligent assistance**: Users don't get hints on how to improve or complement their notes

### Your Solution
**QuickNote AI** is a unified web application that:
- ✅ Automatically analyzes note text and suggests relevant tags
- ✅ Allows quick confirmation, removal, or addition of tags from a fixed set
- ✅ Generates personalized tips from local LLM (Ollama + qwen2.5:1.5b)
- ✅ Provides smart search: ask in your own words → get contextual answer based on your notes
- ✅ Stores everything in PostgreSQL with expandable note cards for full viewing

---

## ⚙️ Features

### Implemented Features (Version 1)
| Feature | Status | Description |
|---------|--------|-------------|
| 📝 Save Note | ✅ | Text → auto-title + auto-tags + AI insight |
| 🏷️ Auto-Tagging | ✅ | Keyword analysis → categories: `study`, `plans`, `work`, `ideas`, `personal`, `important` |
| ✅ Tag Validation | ✅ | Remove extras, add from cloud, max 5 tags |
| 💡 LLM Insight | ✅ | Personalized tip up to 10 words (Ollama, qwen2.5:1.5b) |
| 🔍 Smart Search | ✅ | SQL text search + contextual AI response |
| 📚 History | ✅ | Notes list with expandable full-view cards |
| 🗄️ PostgreSQL | ✅ | Reliable storage with automatic schema migration |
| 🌐 Web Interface | ✅ | Single HTML file, responsive design, no external dependencies |

---

## 🚀 Usage

### How to Use the Product

1.  **Open the application** in browser: `http://<VM-IP>:9999`
2.  **Enter your note** in the text area (e.g., *"Tomorrow database lab, prepare demo"*)
3.  **Click "💾 Save"** → application automatically:
    - Generates title from first 7 words
    - Suggests tags based on keywords (`#study`, `#plans`)
    - Gets AI-powered tip (*"💡 Check DB connection before demo"*)
4.  **Edit tags** (optional):
    - Click `×` on unwanted tag to remove
    - Click tag from cloud to add (max 5)
    - Click **"✅ Confirm"** to save changes
5.  **Find notes** via smart search:
    - Enter query in search field (e.g., *"what did I write about databases?"*)
    - Get contextual AI response + list of found notes
6.  **View history**:
    - Click any note in the list → expands for full viewing

---

## 🐳 Deployment

### Virtual Machine Requirements  
- **OS**: Ubuntu 24.04 (as on university VMs)
- **Architecture**: x86_64
- **RAM**: minimum 2 GB
- **Disk**: minimum 10 GB free space
- **Network**: access to ports 9999 (app), 5432 (DB), 11434 (Ollama)

### Prerequisites on VM

#### Option A: Direct Run (recommended for university VMs)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
sudo apt update && sudo apt install -y postgresql postgresql-contrib
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen2.5:1.5b
```
#### Option B: Docker (for production)
```bash
sudo apt update && sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

### Step-by-Step Deployment Instructions
#### Option 1: Direct Run (without Docker)
```bash
git clone https://github.com/Guzinba/se-toolkit-hackathon.git
cd se-toolkit-hackathon
sudo -u postgres psql -c "CREATE USER quicknote WITH PASSWORD 'quicknote123';"
sudo -u postgres psql -c "CREATE DATABASE quicknote_db OWNER quicknote;"
uv venv
source .venv/bin/activate
uv pip install fastapi sqlmodel httpx uvicorn psycopg2-binary pydantic sqlalchemy
ollama serve &
cd simple_app
uv run uvicorn main:app --host 0.0.0.0 --port 9999
```
#### Option 2: Docker (production)
```bash
git clone https://github.com/Guzinba/se-toolkit-hackathon.git
cd se-toolkit-hackathon
docker-compose up -d --build
docker exec -it quicknote-ollama ollama pull qwen2.5:1.5b
```

#### Health Check
```bash
curl http://localhost:9999/health
curl -X POST http://localhost:9999/api/process -H "Content-Type: application/json" -d '{"content":"Test"}'
```

#### Environment Variables
| Variable | Default | Description |
|---------|--------|-------------|
| DATABASE_URL | postgresql://quicknote:quicknote123@localhost:5432/quicknote_db | PostgreSQL connection |
| OLLAMA_URL | http://127.0.0.1:11434/v1/chat/completions | LLM API endpoint |
