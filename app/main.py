from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host to ensure it's a valid IP address or hostname
        socket.gethostbyname(host)
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except (socket.gaierror, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}