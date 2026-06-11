from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate user input to ensure it does not contain malicious content
        if any(char in request.host for char in [';', '&', '|', '$', '`']):
            return JSONResponse(content={"status": "failed", "error": "Invalid characters in host parameter."}, status_code=400)
        # Use shlex to safely escape the host parameter
        result = subprocess.run(['ping', shlex.quote(request.host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return JSONResponse(content={"status": "completed", "output": result.stdout.decode()}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr.decode()}, status_code=500)