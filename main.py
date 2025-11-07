from routes.authentication import router as auth_router
from routes.group import router as group_router
from routes.expense import router as expense_router
from database import Database
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi_offline import FastAPIOffline
from fastapi import status
import os
app = FastAPIOffline()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # یا آی‌پی دوستت
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(group_router, prefix="/group", tags=["Group"])
app.include_router(expense_router, prefix="/expense", tags=["Expense"])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.get("/", response_class=FileResponse)
async def test():
    file_path = os.path.join(BASE_DIR, "static", "index.html")
    return FileResponse(file_path, status_code=status.HTTP_200_OK)


@app.on_event("startup")
async def startup_db():
    await Database.connect()


@app.on_event("shutdown")
async def shutdown_db():
    await Database.close()
