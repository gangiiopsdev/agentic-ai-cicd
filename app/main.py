from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with full path and shell=False
        result = subprocess.run(['/bin/ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize the input host
    if not all(c.isalnum() or c in '._-' for c in host):
        return {"status": "failed", "error": "Invalid host name"}
    return ping(host)