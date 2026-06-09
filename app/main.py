from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return {'status': safe_ping(host)}
    else:
        return {'error': 'Invalid host'}
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts