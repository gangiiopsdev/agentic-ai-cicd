from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run and shell=False
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)