from fastapi import FastAPI
from app.routers import students
from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.errors import ConflictError, NotFoundError

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


@app.exception_handler(NotFoundError)
def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(ConflictError)
def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(status_code=409, content={"detail": str(exc)})