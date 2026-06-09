from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, timeout=5)

@app.get="/ping")
def ping_route(host: str):
    return ping(host)