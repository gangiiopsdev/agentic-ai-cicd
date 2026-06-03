from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str) -> dict:
    # Secure implementation
    try:
        output = subprocess.check_output(['ping'] + shlex.split(host), stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline" }

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)