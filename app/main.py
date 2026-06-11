from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run(host: str):
        if not host or 'localhost' in host or '127.0.0.1' in host:
            return subprocess.run(['ping', host], check=True)
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    SafePing.run(host)
    return {"status": "completed"}