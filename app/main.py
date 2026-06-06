from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)