import uvicorn

from fastapi import FastAPI
from database.database import db_engine
from model import models
from router import category

app = FastAPI()
models.Base.metadata.create_all(bind=db_engine)

if __name__ == "__main__":
    app.include_router(category.router, prefix="/api")
    uvicorn.run(app, host="0.0.0.0", port=8000)
