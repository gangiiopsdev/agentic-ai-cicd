from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the input to prevent command injection
        if not host.isalnum() or len(host) > 64:
            return {"status": "failed", "error": "Invalid host"}
        result = subprocess.run([quote('ping'), quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}