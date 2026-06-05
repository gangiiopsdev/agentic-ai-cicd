from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '.' in host:
        raise ValueError("Invalid host parameter")

    # Use shlex.quote to safely quote the host parameter
    safe_host = shlex.quote(host)
    try:
        subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": process.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}