# ResolveAI 🤖

An enterprise-grade, LLM-powered Retrieval-Augmented Generation (RAG) troubleshooting assistant specifically engineered for **SAP SuccessFactors Learning Management System (LMS)** support operations.

ResolveAI empowers support teams to rapidly investigate, diagnose, and resolve complex LMS issues by grounding responses in verified resolution playbooks and official SAP Knowledge Base Articles (KBAs).

---

## 🌟 Key Features

* **Grounded RAG Architecture:** Eliminates hallucinations by strictly grounding LLM responses in curated resolution playbooks and official SAP documentation.
* **Intelligent Scenario Retrieval:** Custom semantic chunking preserving troubleshooting sections (`Decision Flow`, `Common Causes`, `Troubleshooting Steps`).
* **Calibrated Relevance Matching:** Rejects out-of-scope inquiries and returns calibrated similarity confidence scores for every source.
* **Deterministic SHA-256 Chunk Fingerprints:** Enables incremental updates without rebuilding the entire database from scratch.
* **Support Engineer UI:** Built-in 1-click copy for ticketing systems (ServiceNow / Jira), quick-action troubleshooting queries, and verified source provenance.
* **Decoupled Client-Server Design:** High-throughput FastAPI REST backend paired with an intuitive Streamlit frontend.

---

## 🧠 System Architecture

```text
User Query (Web UI / API)
        │
        ▼
Domain Routing & Query Embedding (SentenceTransformers all-MiniLM-L6-v2)
        │
        ▼
Vector Similarity Search & Filtering (ChromaDB Persistent Store)
        │
        ├── Score < 25% ──► Out-of-Scope Fallback (No Hallucination)
        │
        ▼ Score ≥ 25%
Enriched Context Assembly + Citations Metadata
        │
        ▼
Grounded Generation (Google Gemini 3.5 / 3.6 Flash via google-genai SDK)
        │
        ▼
Structured Output (Root Causes, Step-by-Step Resolution, Ticket-Ready Markdown)
```

---

## 📚 Knowledge Base Coverage

ResolveAI features 13 deep-domain expert playbooks and official SAP KBAs across core SAP SuccessFactors LMS modules:

* **Assignment Profiles & Rules:** Automatic assignments, criteria changes, multiple profiles conflict.
* **Curriculum & Retraining:** Recurring training requirements, retraining intervals, completion handling.
* **User Connector & Data Sync:** SF User Connector sync delays, active in HR/PD but missing/inactive in LMS.
* **Online Content & SCORM:** Tracking issues, completion failures, AICC/SCORM cross-domain communication.
* **Access & Security:** Role-based permissions, MyLearning tile visibility, Single Sign-On (SSO) & login validation.
* **Class & Scheduled Offerings:** Enrollment limits, waitlist processing, completion status updates.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **LLM Inference** | Google Gemini (`gemini-3.5-flash` / `gemini-3.6-flash`) |
| **LLM SDK** | `google-genai` |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` (384 dims) |
| **Vector Store** | `ChromaDB` (Persistent) |
| **API Backend** | `FastAPI`, `Uvicorn`, `Pydantic v2` |
| **Frontend UI** | `Streamlit` |
| **Configuration** | `pydantic-settings` |

---

## 🚀 Quick Start (Local Setup)

### 1. Clone & Setup Virtual Environment
```bash
git clone https://github.com/TejalGB/ResolveAI.git
cd ResolveAI

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Create a `.env` file in the project root:
```ini
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash
RESOLVEAI_API_URL=http://127.0.0.1:8000
```

### 3. Initialize & Index Knowledge Base
Run the unified ingestion pipeline to chunk documents and index them into ChromaDB:
```bash
python -m src.ingestion.pipeline --reindex
```

### 4. Start the Application

**Terminal 1 (Backend API):**
```bash
uvicorn src.api.main:app --reload --port 8000
```

**Terminal 2 (Frontend UI):**
```bash
streamlit run app.py
```
Visit `http://localhost:8501` to access ResolveAI.

---

## 📡 API Reference

### Health Check
* **GET** `/`
* **Response:**
  ```json
  { "message": "ResolveAI API is running successfully." }
  ```

### Ask Question
* **POST** `/ask`
* **Request Body:**
  ```json
  { "question": "Course assigned again after completion" }
  ```
* **Response Body:**
  ```json
  {
    "answer": "### Possible Causes\n1. Curriculum retraining rule configured...",
    "sources": [
      {
        "source": "curriculum_retraining.md",
        "scenario": "Common Causes and Resolution",
        "category": "Curriculum and Retraining",
        "match_score": 67.6
      }
    ]
  }
  ```

---

## ☁️ Cloud Deployment Guide

ResolveAI is designed for decoupled cloud deployment:

### Backend (Render.com)
1. Create a **New Web Service** from your GitHub repo.
2. **Runtime:** `Python 3`
3. **Build Command:**
   ```bash
   pip install -r requirements.txt && python -m src.ingestion.pipeline --reindex
   ```
4. **Start Command:**
   ```bash
   uvicorn src.api.main:app --host 0.0.0.0 --port $PORT
   ```
5. **Environment Variables:**
   * `GEMINI_API_KEY`: `your_key`
   * `GEMINI_MODEL`: `gemini-3.5-flash`

### Frontend (Streamlit Community Cloud)
1. Deploy `app.py` directly from your GitHub repo on [share.streamlit.io](https://share.streamlit.io).
2. In **App Settings > Secrets**, set:
   ```toml
   RESOLVEAI_API_URL = "https://your-backend-name.onrender.com"
   ```

---

## 🔮 Future Enhancements

- [ ] **Multi-Turn Contextual Query Rewriting:** Preserve conversation history across multi-turn troubleshooting dialogues.
- [ ] **Streaming Responses (SSE):** Stream tokens in real time to the web interface.
- [ ] **Hybrid Search (BM25 + Dense Vectors):** Implement Reciprocal Rank Fusion (RRF) for enhanced technical keyword precision.
- [ ] **Feedback & Audit Logging:** Support engineer ratings (👍 / 👎) logged to a database for continuous knowledge base refinement.

---

## 📄 License
Internal & Proprietary — Developed for SAP SuccessFactors Support Automation.
