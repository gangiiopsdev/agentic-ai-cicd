from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['example.com', 'localhost']:  # Example allowed hosts
        return True
    return False

@app.get("/ping")
def ping(host: str):

    if safe_ping(host):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

    return {"status": "completed"}