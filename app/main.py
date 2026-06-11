from fastapi import FastAPI
import subprocess
class Config:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in Config.ALLOWED_HOSTS:
        raise HTTPException(status_code=400, detail="Host is not allowed")
    subprocess.call(["ping", host])
    return {"status": "completed"}