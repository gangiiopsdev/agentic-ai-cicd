from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(host):
    if not host.isalnum() or len(host) > 50:
        return None
    return shlex.quote(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is None:
        return {"status": "failed", "error": "Invalid input"}
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}