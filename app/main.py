from fastapi import FastAPI
import subprocess
app = FastAPI()
def execute_ping(host):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], capture_output=True, text=True)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid hostname"}, 400
    # Use parameterized command to avoid shell injection
    subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed"}