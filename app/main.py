from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and executable specified
    subprocess.call(['ping', host], shell=False, executable='/bin/ping')

@app.get("/ping")
def ping_endpoint(host: str):
    response = ping(host)
    return {"status": "completed"}