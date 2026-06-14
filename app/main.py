from fastapi import FastAPI
import subprocess
glitchy_api = FastAPI()
@glitchy_api.get("/ping")
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}