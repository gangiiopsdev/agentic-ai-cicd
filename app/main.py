from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Using subprocess.run for a safer alternative with shell=False and argument unpacking
    subprocess.run(['ping', host], shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}