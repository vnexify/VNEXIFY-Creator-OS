from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.router import router as api_router

app = FastAPI(title="VNEXIFY Creator OS Backend")

# Enable CORS for local Electron & React dev server requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "0.1"
    }

app.include_router(api_router, prefix="/api")
