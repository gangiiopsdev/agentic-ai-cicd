from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    subprocess.run(['ping', host], check=True)

app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return {'result': 'Pinging ' + host}