from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        subprocess.call(['ping', host], timeout=5)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)