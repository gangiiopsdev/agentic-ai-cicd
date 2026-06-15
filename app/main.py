from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is None:
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', f'--{sanitized_host}'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "stdout": e.stdout.decode(), "stderr": e.stderr.decode()}