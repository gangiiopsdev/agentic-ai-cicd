from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using shell=False and args parameter
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)