from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.isdigit():
        return {'error': 'Invalid input'}
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping_route(host: str):
    return ping(host)