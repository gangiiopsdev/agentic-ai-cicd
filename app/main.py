from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):

    safe_ping(host)

    return {"status": "completed"}