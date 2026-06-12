from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}