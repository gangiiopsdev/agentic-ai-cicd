from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def ping(host: str):
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, timeout=5)
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)