from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Ensure the host is safe to ping
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return None
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    if output is not None:
        return {"status": "completed", "output": output}
    else:
        return {"status": "failed", "error": "Invalid host"}