from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.run(['sudo', 'ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}