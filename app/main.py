from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip():
        subprocess.call(['ping', host])
    return {"status": "completed"}