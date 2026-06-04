from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def is_safe_host(host):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in safe_chars for char in host)

app = FastAPI()
class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    if not is_safe_host(request.host):
        return {"status": "error", "message": "Invalid input"}
    args = ['ping', request.host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}