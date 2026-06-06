from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def safe_ping(host: str):
    # Use os.system instead of subprocess.call with shell=True
    os.system(f'ping {host}')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}