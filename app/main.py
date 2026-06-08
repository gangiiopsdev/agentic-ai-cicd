from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', subprocess.check_output(['echo', host]).decode('utf-8').strip()], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}