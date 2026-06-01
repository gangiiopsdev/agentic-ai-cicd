from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

def is_valid_host(host: str) -> bool:
    # Add validation logic here
    valid_hosts = ['example.com', 'test.com']
    return host in valid_hosts