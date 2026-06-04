from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None:
        return {"message": "No host specified"}
    # Secure implementation
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}