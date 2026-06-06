from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with args parameter
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_route(host: str):  
    return ping(host)