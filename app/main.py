from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr.decode('utf-8')}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.replace('.', '').isnumeric() or '.' not in host or len(host.split('.')) != 4:
        return {'error': 'Invalid hostname'}
    return safe_ping(host)