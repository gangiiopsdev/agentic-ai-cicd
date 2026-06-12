from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return JSONResponse(content={"status": "failed", "error": "Unsafe host"}, status_code=403)
    try:
        output = subprocess.run(["ping", host], capture_output=True, text=True, check=True, shell=False)
        return JSONResponse(content={"status": "completed", "output": output.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": str(e)}, status_code=500)