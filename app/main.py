from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host])
    else:
        return {"error": "Access denied for host"}
    
    return {"status": "completed"}