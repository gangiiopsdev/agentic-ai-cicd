from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent injection attacks
        if not validate_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts