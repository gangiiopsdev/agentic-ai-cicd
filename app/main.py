from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts or use more sophisticated validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', '--', host]
        subprocess.run(args, check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400