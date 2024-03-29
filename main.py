import uvicorn

from fastapi import FastAPI
from database.database import db_engine
from model import models
from router import category, supplier
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=db_engine)

origins = [
    "http://the100.vn",
    "https://the100.vn",
    "http://localhost",
    "http://localhost:2210",
    "http://103.241.43.112:2210",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    app.include_router(category.router, prefix="/api")
    app.include_router(supplier.router, prefix="/api")
    uvicorn.run(app, host="0.0.0.0", port=2210)
