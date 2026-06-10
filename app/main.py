from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or ' ' in host:
        return 'Invalid host'
    try:
        response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)