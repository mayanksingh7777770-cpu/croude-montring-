
from fastapi import FastAPI
from api.routes import router
from core.database import Base, engine

app = FastAPI(title="AI Crowd Monitoring System")

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Crowd Monitoring System Running"}
