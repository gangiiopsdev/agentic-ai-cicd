from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using list for the command arguments and validating input
    if not host.strip():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):    return {'status': 'completed'}