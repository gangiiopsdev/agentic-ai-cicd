from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Simple example of host validation
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        if sanitize_host(host):
            output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}