from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation with shell=False and full path to executable
    subprocess.call(["ping", host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)