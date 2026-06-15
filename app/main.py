from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'result': 'Pong'}