from fastapi import FastAPI
import subprocess
global app
app = FastAPI()
def secure_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.run(['ping', '--', host], check=True, shell=False)
@app.get("/ping")
def ping(host: str):
    try:
        return secure_ping(host)
    except Exception as e:
        return str(e)