from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        args = ['ping', host]
        subprocess.call(args)
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