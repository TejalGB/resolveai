# ResolveAI 🤖

An enterprise-grade, LLM-powered Retrieval-Augmented Generation (RAG) troubleshooting assistant specifically engineered for **SAP SuccessFactors Learning Management System (LMS)** support operations.

ResolveAI empowers support teams to rapidly investigate, diagnose, and resolve complex LMS issues by grounding responses in verified resolution playbooks and official SAP Knowledge Base Articles (KBAs).

---

## 🌟 Key Features

* **Grounded RAG Architecture:** Eliminates hallucinations by strictly grounding LLM responses in curated resolution playbooks and official SAP documentation.
* **Intelligent Scenario Retrieval:** Custom semantic chunking preserving troubleshooting sections (`Decision Flow`, `Common Causes`, `Troubleshooting Steps`).
* **Calibrated Relevance Matching:** Rejects out-of-scope inquiries and returns calibrated similarity confidence scores for every source.
* **Deterministic SHA-256 Chunk Fingerprints:** Enables incremental updates without rebuilding the entire database from scratch.
* **Support Engineer UI:** Built-in 1-click copy for ticketing systems (ServiceNow), quick-action troubleshooting queries, and verified source provenance.
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
| **LLM Model** | Google Gemini (`gemini-3.6-flash`) |
| **Embeddings** | `sentence-transformers/all-MiniLM-L6-v2` |
| **Vector Database** | `ChromaDB` |
| **API Backend** | `FastAPI`, `Uvicorn`, `Pydantic` |
| **Frontend UI** | `Streamlit` |

---

## 🎯 Key Capabilities Demonstrated

* **End-to-End RAG Architecture:** Designed and built a complete Retrieval-Augmented Generation pipeline connecting domain documents to an LLM.
* **Vector Search & Embeddings:** Implemented semantic search using ChromaDB and SentenceTransformers (`all-MiniLM-L6-v2`) with custom similarity scoring.
* **Data Ingestion & Chunking:** Created an automated pipeline to clean, deduplicate, and chunk technical documents into structured knowledge vectors.
* **Prompt Engineering & Grounding:** Engineered prompts with strict guardrails to prevent hallucinations and enforce factual, step-by-step troubleshooting.
* **REST API Development:** Built asynchronous backend endpoints using FastAPI and Pydantic for clean data validation and structured responses.
* **Full-Stack AI Prototyping:** Developed an interactive Streamlit user interface featuring source attribution, match confidence, and 1-click ticket copying.
* **Performance & Optimization:** Implemented SHA-256 fingerprinting for incremental data updates, preventing expensive database rebuilds.

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
GEMINI_MODEL=gemini-3.6-flash
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

## 📄 License
Internal & Proprietary — Developed for SAP SuccessFactors Support Automation.
