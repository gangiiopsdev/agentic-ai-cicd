from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if host == 'localhost':
        args = ['ping', host]
        subprocess.call(args)
    return {'status': 'completed'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)