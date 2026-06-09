from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost':
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'status': 'invalid host'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)