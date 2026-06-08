from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid hostname"}
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {"status": "completed"}