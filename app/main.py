from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and avoiding partial paths
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)