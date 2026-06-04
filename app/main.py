from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input before using in subprocess call
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str): 
    return ping(host)