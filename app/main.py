from fastapi import FastAPI
import subprocess
global_lock = subprocess.DEVNULL
def safe_ping(host):
    try:
        args = ['ping', host]
        if subprocess.call(args, stdout=global_lock, stderr=global_lock) != 0:
            return {'status': 'failure'}
        else:
            return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)