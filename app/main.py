from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.example.com']

@app.get("/ping")
def ping(host: str):
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Host not allowed")