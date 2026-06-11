from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        raise ValueError('Invalid host')