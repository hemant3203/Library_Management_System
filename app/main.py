from fastapi import FastAPI
from app.routers import students

from app.core.config import settings


app=FastAPI(
    title=settings.app_name,
    version=settings.version,
)
app.include_router(students.router)


@app.get("/health")
def health_check():
    return {
        "status":"ok",
        "app_name":settings.app_name,
        "version":settings.version,
    }