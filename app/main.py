from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define a whitelist of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}