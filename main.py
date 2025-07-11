from fastapi import FastAPI
from routes.authentication import router as auth_router
from routes.group import router as group_router
from routes.expense import router as expense_router
from database import Database
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi_offline import FastAPIOffline

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


@app.on_event("startup")
async def startup_db():
    await Database.connect()


@app.on_event("shutdown")
async def shutdown_db():
    await Database.close()
