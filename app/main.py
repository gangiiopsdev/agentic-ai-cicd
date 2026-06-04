from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if ' ' in host or '\' in host:
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(["ping", host])
    return {"status": "completed"}