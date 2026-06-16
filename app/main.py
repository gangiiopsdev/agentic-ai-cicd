from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

@app.get("/ping")
def ping(credentials: HTTPBasicCredentials = Depends(security)):
    # Sanitize input to prevent command injection
    safe_host = subprocess.list2cmdline([credentials.username])
    try:
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}