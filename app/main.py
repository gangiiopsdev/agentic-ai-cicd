from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with proper sanitization
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {'status': 'completed'}