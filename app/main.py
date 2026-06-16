from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def get_ping(host: str): 
    return ping(host)