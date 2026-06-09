from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with exit code {e.returncode}'}, 400

@app.get("/ping")
def ping_route(host: str):
    return ping(host)