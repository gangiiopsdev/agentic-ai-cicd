from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using shell=False and list arguments
    args = ['ping', host]
    subprocess.call(args)

@app.get="/ping")
def ping(host: str):
    return ping(host)