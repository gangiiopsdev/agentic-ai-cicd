from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "output": "Invalid hostname"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)