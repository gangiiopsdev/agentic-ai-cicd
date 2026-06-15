from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]{1,100}$', host):
        raise ValueError("Invalid hostname")
    cmd = ['ping', *shlex.split(host)]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}