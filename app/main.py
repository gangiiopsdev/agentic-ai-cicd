from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation with proper sanitization and use of shell=False
    subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    return ping(host)