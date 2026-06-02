from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = quote(host)
    try:
        result = subprocess.run(["ping", safe_host], capture_output=True, text=True, timeout=5)
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)