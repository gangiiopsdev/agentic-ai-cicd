from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com', 'another.example.com']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return ' '.join(['ping', '-c', '1', host])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        result = subprocess.run(safe_ping(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}