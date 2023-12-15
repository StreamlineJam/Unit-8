from fastapi import FastAPI
import uvicorn

import models
from database import engine

from routers import tasks

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(tasks.router, prefix="/tasks")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
