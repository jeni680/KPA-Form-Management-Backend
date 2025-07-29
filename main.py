from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import kpaform  # ✅ Import your router
from app.database import engine
from app import models

app = FastAPI(
    title="KPA API",
    version="0.1.0"
)

# ✅ Add CORS middleware (optional if already in app.py)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Register the router with a prefix and tag
app.include_router(kpaform.router, prefix="/api", tags=["KPAForm"])

# ✅ Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "KPA API is running!"}
models.Base.metadata.create_all(bind=engine)