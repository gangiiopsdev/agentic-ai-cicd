from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"status": "failed", "error": "Invalid host name"}
    try:
        result = subprocess.run(["ping", *host.split()], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}