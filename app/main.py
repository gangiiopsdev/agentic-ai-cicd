from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric():
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid input'}

@app.get("/ping")
def ping(host: str):