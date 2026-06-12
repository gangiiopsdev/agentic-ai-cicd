from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host: str):
        allowed_hosts = ['localhost', '127.0.0.1']
        if not host or host in allowed_hosts:
            return subprocess.run(['ping', '-c 1', host], check=True)
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    SafePing.run(host)
    return {"status": "completed"}