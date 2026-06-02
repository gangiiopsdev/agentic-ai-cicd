from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', validated_host], capture_output=True, text=True, check=True)
        return {'host': validated_host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}