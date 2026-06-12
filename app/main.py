from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {"error": "Host is required and cannot be empty."}
    args = ["ping", host]
    subprocess.call(args, shell=False)
    return {"status": "completed"}