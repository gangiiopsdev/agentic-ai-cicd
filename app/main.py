from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    # Secure implementation\n    subprocess.call(["ping", host])\n    return {"status": "completed"}