from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)