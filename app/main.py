from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['example.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ALLOWED_HOSTS:
        subprocess.call(f'ping {host}', shell=False)
    else:
        raise HTTPException(status_code=403, detail="Unauthorized host")
    return {"status": "completed"}