from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_result = safe_ping(host)
    return {"status": "completed", "result": safe_ping_result}