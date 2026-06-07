from fastapi import FastAPI
import subprocess
git

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'Pinging', 'host': host}