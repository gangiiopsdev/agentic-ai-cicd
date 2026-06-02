from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    try:
        args = shlex.split(f'ping {safe_host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}