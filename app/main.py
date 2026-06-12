from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        output, error = process.communicate()
        return {"status": "completed", "output": output.decode(), "error": error.decode() if error else None}
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
        return {"status": "failed", "error": str(e)}