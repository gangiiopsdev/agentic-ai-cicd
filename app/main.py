from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    return ' '.join(host.split())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if '@' not in sanitized_host:
        try:
            result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr.decode()}
    else:
        return {'status': 'error', 'message': 'Invalid host'}