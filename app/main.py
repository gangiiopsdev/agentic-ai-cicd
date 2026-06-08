from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using safe method
    subprocess.run(['ping', host], check=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'Pinging ' + host}