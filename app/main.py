from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):

    # Using the safe implementation
    safe_ping(host)

    return {"status": "completed"}