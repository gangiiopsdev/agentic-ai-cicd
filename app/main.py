from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)