from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping_safe(host: str):
    return ping(host)