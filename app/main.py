from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def validate_host(host: str) -> bool:
    # Add validation logic here to ensure host is safe
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return JSONResponse(status_code=400, content={"error": "Invalid host"})
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return JSONResponse(content={"status": "completed", "output": result.stdout.strip()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"error": str(e)})