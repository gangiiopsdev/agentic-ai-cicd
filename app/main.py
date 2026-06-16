from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get="/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {'status': 'error', 'message': 'Invalid host'}

    # Secure implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}