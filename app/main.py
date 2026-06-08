from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of os.system
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}