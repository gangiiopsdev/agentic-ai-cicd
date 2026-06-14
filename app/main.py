from fastapi import FastAPI
import subprocess
def safe_host(host: str) -> str:
    allowed_hosts = ['ping', 'localhost']
    return host if host in allowed_hosts else 'localhost'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str = 'localhost'):
    safe_host_value = safe_host(host)
    try:
        output = subprocess.run([safe_host_value], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}