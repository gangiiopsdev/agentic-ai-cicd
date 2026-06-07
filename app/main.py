from fastapi import FastAPI
import os

global app = FastAPI()

def ping(host: str):
    # Secure implementation
    response = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return response.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)