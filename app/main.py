from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input for ping')

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}