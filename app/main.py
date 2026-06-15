from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host name"}

    # Use a full path for the executable to mitigate command injection risks
    result = subprocess.run(['/bin/ping', host], capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": result.stderr}