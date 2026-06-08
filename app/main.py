from fastapi import FastAPI
import subprocess

class HostValidator:
    allowed_hosts = ['127.0.0.1', 'localhost']

    @staticmethod
def validate_host(host):
        if host in HostValidator.allowed_hosts:
            return True
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    HostValidator.validate_host(host)
    try:
        # Use a whitelist of allowed hosts for ping
        if host in ['127.0.0.1', 'localhost']:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Invalid host for ping')
    except subprocess.CalledProcessError as e:
        raise ValueError('Ping failed') from e