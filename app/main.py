from fastapi import FastAPI
import subprocess
from fastapi.params import Query

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit() and '.' in host and '-' in host:
        return False
    return True

@app.get("/ping")
def ping(host: str = Query(..., min_length=1, regex='^[a-zA-Z0-9.-]+$')):
    if safe_ping(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": e.stderr}
    else:
        return {"status": "failed", "error": "Invalid host parameter"}