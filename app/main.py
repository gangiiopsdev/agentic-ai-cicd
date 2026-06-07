from fastapi import FastAPI
import subprocess
import shlex

global safe_hosts
safe_hosts = set()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global safe_hosts
    if host not in safe_hosts:
        # Sanitize input to avoid command injection
        try:
            subprocess.check_output(['ping', '-c', '1', shlex.quote(host)], stderr=subprocess.STDOUT)
            safe_hosts.add(host)
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e.output)}
    return {"status": "completed"}