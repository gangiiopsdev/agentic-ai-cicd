from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)