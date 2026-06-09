from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts or patterns
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', *shlex.split(host)]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}