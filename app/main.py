from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)