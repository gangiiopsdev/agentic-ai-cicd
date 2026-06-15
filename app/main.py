from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from shlex import quote as safe_quote

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    if any(char in host for char in [';', '&', '|', '$', '`']):
        raise ValueError("Invalid characters in host parameter")

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        result = subprocess.run(['ping', safe_quote(request.host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={"status": "completed", "output": result.stdout.decode()}, status_code=200)
    except (subprocess.CalledProcessError, ValueError) as e:
        return JSONResponse(content={"status": "failed", "error": str(e)}, status_code=500)