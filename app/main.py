from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and safe execution
    if host.isalnum():
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid hostname"}