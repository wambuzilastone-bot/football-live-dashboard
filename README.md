# Football Live Dashboard

A full-stack web app for live football fixtures, standings, and stats (GF/GA) using real-time scraped data from BetExplorer.

## Project structure

- `backend/` — FastAPI Python app for API & web scraping
- `frontend/` — React (Vite) app with monospace font layout

## Setup

### 1. Backend (FastAPI)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

## Deployment

This project is ready for Vercel (frontend) and can be adapted for Vercel serverless backend.

---

## Customization

- Monospace font (`font-family: 'Fira Mono', 'Menlo', 'Monaco', 'Consolas', monospace`) applied globally.
- Extend API endpoints and UI as needed for more data.