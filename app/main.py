from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def is_safe_host(host):
    # Implement your logic to check if the host is safe
    return True

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return JSONResponse(content={"error": "Host is not safe"}, status_code=400)
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, timeout=5, check=True, shell=False)
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)