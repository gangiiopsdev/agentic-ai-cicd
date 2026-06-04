from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isdigit():
        return {'error': 'Invalid input'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.call(['ping', host], shell=False)
        if result == 0:
            return {'status': 'completed'}
        else:
            return {'status': 'failed'}
    except Exception as e:
        return {'error': str(e)}