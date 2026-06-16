from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    allowed_hosts = ['8.8.8.8', '192.168.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        return JSONResponse(content={"status": "failed", "error": "Invalid host"}, status_code=400)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr}, status_code=500)