from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' not in host:
        return JSONResponse(status_code=400, content={"status": "failed", "error": "Invalid host parameter"})
    try:
        output = subprocess.check_output(['ping', '-c', '1', f'--{host}'], stderr=subprocess.STDOUT, text=True)
        return JSONResponse(status_code=200, content={"status": "completed", "output": output})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"status": "failed", "error": str(e)})