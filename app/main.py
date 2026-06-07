from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)