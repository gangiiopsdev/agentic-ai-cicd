from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == '127.0.0.1':
        return True
    else:
        raise ValueError('Ping to non-localhost hosts is not allowed')

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(['ping', '-c 4', host], check=True, shell=False)
    return {"status": "completed"}