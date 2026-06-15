from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', subprocess.list2cmdline([host])], shell=False)