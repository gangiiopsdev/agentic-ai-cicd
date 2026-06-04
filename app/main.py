from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not host or ' ' in host or '\' in host or '"' in host:
        return {"error": "Invalid input"}
    subprocess.call(['ping', host])
    return {"status": "completed"}