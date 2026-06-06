from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c 1', host]  # Limit the number of pings to mitigate potential DoS
    result = subprocess.run(args, capture_output=True, text=True, check=True)  # Use check=True to handle errors gracefully
    return {'status': 'completed', 'output': result.stdout}