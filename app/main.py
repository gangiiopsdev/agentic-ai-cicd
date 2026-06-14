from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = ['ping', '-c', '1'] + shlex.split(host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)