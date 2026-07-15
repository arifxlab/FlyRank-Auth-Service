from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.core.config import settings

from app.api.protected import router as protected_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "FlyRank Auth Service is running!"
    }

app.include_router(auth_router)
app.include_router(protected_router)