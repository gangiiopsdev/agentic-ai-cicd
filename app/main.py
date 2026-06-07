from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            args = ['ping', '-c', '1', host]  # Use the provided host directly instead of hostname
            subprocess.run(args, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host'}