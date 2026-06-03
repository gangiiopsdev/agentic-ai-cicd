from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host or 'ping' in host:
        raise ValueError('Invalid host')
    # Sanitize the host input to prevent command injection
    host = ''.join(filter(str.isalnum, host))
    cmd = ['ping', '-c', '1', shlex.quote(host)]
    return subprocess.run(cmd, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}