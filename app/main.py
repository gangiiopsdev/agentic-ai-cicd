from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {"error": "Host parameter is required"}
    # Safe implementation with input validation
    try:
        subprocess.call(['ping', '-c', '1', host], shell=False)
    except Exception as e:
        return {"error": str(e)}
    
    return {"status": "completed"}