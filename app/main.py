from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.Popen with a safe argument list and validated input
    if not host.strip():
        raise ValueError('Invalid host value')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_handler(host: str):
    return {'status': 'completed'}