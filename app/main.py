from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = {'example.com', 'localhost'}

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        raise HTTPException(status_code=403, detail="Host not allowed")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}