from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']  # Define a list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        try:
            subprocess.run(['ping', host], check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            print(f'Ping failed with error: {e}')
            return {'status': 'failed'}
    else:
        return {'status': 'failed', 'message': 'Host not allowed'}