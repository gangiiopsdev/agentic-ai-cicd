from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    allowed_hosts = ["example.com", "test.com"]
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host"}

    # Use shlex.quote to safely escape the host input
    try:
        output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}