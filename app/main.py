from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not host.isalnum():
        return {"status": "error", "message": "Invalid hostname"}
    try:
        result = subprocess.run([shell_quote('ping'), shell_quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stderr": e.stderr.decode()}