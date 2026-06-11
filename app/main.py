from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if '-' in host:
        return "Invalid input"
    # Use shlex.quote to sanitize the input
    return subprocess.run(shlex.quote('ping') + ' ' + shlex.quote(host), capture_output=True, text=True, shell=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result.returncode == 0:
        return {"status": "completed", "result": result.stdout}
    else:
        return {"error": result.stderr}