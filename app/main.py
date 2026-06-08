from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)