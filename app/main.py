from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "127.0.0.1"]  # List of allowed hosts
    if host not in allowed_hosts:
        return JSONResponse(status_code=400, content={"error": "Invalid host"})
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"error": e.output.decode()})