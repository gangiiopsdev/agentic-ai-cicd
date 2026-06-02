from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {"error": "Invalid input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}