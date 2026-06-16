from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost", "127.0.0.1"}

def safe_ping(host):
    if host in globally_allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.stderr}
    else:
        return {'status': 'invalid host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if '/' not in host and '@' not in host and not host.startswith('127.0.0.') and not host.startswith('::ffff:127.0.0.'):  # Basic validation
        return safe_ping(host)
    else:
        return {'status': 'invalid host'}