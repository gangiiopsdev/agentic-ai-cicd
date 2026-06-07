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
        # Validate the host input to ensure it does not contain malicious content
        if not host.isalnum() or '.' not in host:
            return {"status": "failed", "error": "Invalid host format"}
        subprocess.run(["ping", quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}