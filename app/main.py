from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to avoid command injection
    if not host.strip() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host parameter"}
    try:
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}