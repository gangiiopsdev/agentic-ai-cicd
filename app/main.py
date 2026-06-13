from fastapi import FastAPI
import subprocess
app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}