from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    else:
        return False

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'error': 'Invalid host'}, 400