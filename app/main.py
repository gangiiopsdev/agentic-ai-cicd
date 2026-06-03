from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

def safe_ping(host: str):
    command = ['ping', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return JSONResponse(content={"status": "completed", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": str(e)}, status_code=500)

app = FastAPI()

allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": str(e)}, status_code=500)