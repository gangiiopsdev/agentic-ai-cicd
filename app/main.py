from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)