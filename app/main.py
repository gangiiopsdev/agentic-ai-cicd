from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safer implementation using subprocess.run with shell=False and validation
    if host.startswith(('192.168.', '10.0.', '172.')) or host in ['localhost', '127.0.0.1']:
        try:
            result = subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'invalid_host'}