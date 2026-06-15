from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation, allow only alphanumeric characters and periods
    return all(c.isalnum() or c == '.' for c in host)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400