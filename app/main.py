from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    try:
        subprocess.call(["ping", host], shell=False)
    except Exception as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}