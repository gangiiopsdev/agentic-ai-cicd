from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = quote(host)
        output = subprocess.check_output(["ping", safe_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.output.decode()}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "error": "Operation timed out"}