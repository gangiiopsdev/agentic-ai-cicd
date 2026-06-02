from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and validation
    if host == 'localhost':
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}