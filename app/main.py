from fastapi import FastAPI
import subprocess

async def validate_host(host):
    return host.isalnum()

def safe_ping(host):
    allowed_hosts = ['example.com', 'localhost']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid input')
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid input'}, 400
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'error': str(e)}, 400