from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
given_safe_hosts = {"example.com", "localhost"}  # Define safe hosts

app = FastAPI()

@app.get("")
def home():
    return JSONResponse(content={"message": "Agentic Self-Healing Pipeline"})

@app.get("/ping")
def ping(host: str):
    if host in given_safe_hosts:
        try:
            subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return JSONResponse(content={"status": "completed"})
        except subprocess.CalledProcessError as e:
            return JSONResponse(content={"error": str(e.stderr.decode())}, status_code=500)
    else:
        return JSONResponse(content={"error": "Unauthorized host"}, status_code=403)