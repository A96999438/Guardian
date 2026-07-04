from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes.scan_routes import router as scan_router
from app.routes.gmail_routes import router as gmail_router
from app.services.phishtank_service import load_phishtank_data
from app.core.scheduler import start_scheduler, shutdown_scheduler

load_dotenv()

app = FastAPI(title="Guardian Backend")

# =========================
# STARTUP
# =========================
@app.on_event("startup")
async def startup():
    load_phishtank_data()
    start_scheduler()

# =========================
# SHUTDOWN (FIXES CancelledError)
# =========================
@app.on_event("shutdown")
def shutdown():
    shutdown_scheduler()

# =========================
# ROUTES
# =========================
app.include_router(scan_router, prefix="/guardian")
app.include_router(gmail_router, prefix="/guardian/gmail")

@app.get("/")
def root():
    return {"status": "Guardian Backend Running"}
