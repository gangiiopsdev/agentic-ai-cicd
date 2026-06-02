from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host parameter
    if host.strip() != host or ' ' in host:
        return{"error": "Invalid input"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}