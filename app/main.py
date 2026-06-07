from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not host.isalnum() or '..' in host:
        return {"status": "failed", "error": "Invalid host parameter"}
    try:
        output = subprocess.check_output(['ping', subprocess.list2cmdline([host])], stderr=subprocess.STDOUT, universal_newlines=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}