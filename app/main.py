from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex to avoid shell injection
    try:
        subprocess.check_call(['ping'] + shlex.split(host), timeout=10)
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping failed with error: {e}'}
    return {"status": "completed"}