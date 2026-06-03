from fastapi import FastAPI
import subprocess
import shlex
import re
global app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
    try:
        args = shlex.split(f'ping {safe_host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}