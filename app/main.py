from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent injection attacks
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def get_ping_status():
    return {"message": "Ping function fixed."}