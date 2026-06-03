from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, text=True, capture_output=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}
    else:
        return {'status': 'error', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)