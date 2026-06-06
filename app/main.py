from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    return host in allowed_hosts

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return JSONResponse(content={"status": "failed", "error": "Invalid host"}, status_code=400)
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return JSONResponse(content={"status": "completed", "output": output.decode()}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.output.decode()}, status_code=500)