from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate host to ensure it does not contain malicious content
    if not host.strip().isalnum():
        raise ValueError("Invalid hostname")
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)