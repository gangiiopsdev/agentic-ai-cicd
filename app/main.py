from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    if not host.isalnum():
        return {"error": "Invalid host"}
    args = ['ping', f'--{host}']  # Use a safe way to pass the argument
    subprocess.call(args)
    return {"status": "completed"}