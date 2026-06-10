from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if all(c.isalnum() or c in ('.', '-', '_') for c in host):
        subprocess.call(["ping", host])
    return {"status": "completed"}