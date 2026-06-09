from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
domains = ['google.com', 'example.com']
if host in domains:
        cmd = ['ping', host]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'Pinging ' + host}