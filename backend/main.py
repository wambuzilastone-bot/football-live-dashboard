from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Football Live Dashboard API",
    description="API for scraping and serving live football data from BetExplorer.",
)

# Allow frontend to call backend while developing locally
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Football Live Dashboard API is running!"}

# TODO: Add endpoints for country/league/fixtures/standings/GF/GA
