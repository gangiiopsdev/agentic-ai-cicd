from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)