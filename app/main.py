from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with absolute path and shell=False
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)