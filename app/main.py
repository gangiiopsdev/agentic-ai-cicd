from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    safe_hosts = ['localhost', '127.0.0.1']  # Example of whitelisting safe hosts
    if host in safe_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}
    return {'status': 'error', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)