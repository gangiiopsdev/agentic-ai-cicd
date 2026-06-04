from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if 'ping' in host:
        return {'status': 'error', 'message': 'Illegal command'}
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)