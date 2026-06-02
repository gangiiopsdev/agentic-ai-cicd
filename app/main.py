from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str) -> dict:
    if not host.isnumeric():
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {"status": "completed"}