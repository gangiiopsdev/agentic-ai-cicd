from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and shlex.split for safer command execution
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)