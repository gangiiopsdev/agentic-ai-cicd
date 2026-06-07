from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    try:
        args = shlex.split('ping ' + shlex.quote(host))
        output = subprocess.run(args, capture_output=True, text=True, timeout=5)
        if output.returncode == 0:
            return {"status": "completed", "output": output.stdout}
        else:
            return {"status": "failed", "error": output.stderr}
    except subprocess.TimeoutExpired as e:
        return {"status": "failed", "error": "Command timed out"}