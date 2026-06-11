from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    if '@' in host or '//' in host:
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'status': 'Ping initiated to', 'host': host}