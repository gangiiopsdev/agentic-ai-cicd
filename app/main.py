from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', '-c', '4', host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return secure_ping(host)