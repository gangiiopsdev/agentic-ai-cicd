from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}