from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    try:
        # Validate the input to ensure it does not contain malicious content
        if any(char in host for char in [';', '&', '|', '&&', '||']):
            return {"status": "failed", "error": "Invalid characters in input"}
        subprocess.call(["ping", host], shell=False)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}