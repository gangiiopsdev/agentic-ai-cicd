from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host:
        return {"status": "invalid input"}
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}