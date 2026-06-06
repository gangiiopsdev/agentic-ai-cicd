from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host])

@app.get('/ping')
def ping_route(host: str):
    return ping(host)