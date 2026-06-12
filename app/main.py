from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    return ['ping', '-c', '1', host]

def is_valid_host(host):
    valid_hosts = ['example.com', 'localhost']
    return host in valid_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    command = generate_ping_command(host)
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    if result.returncode != 0:
        return {'status': 'failed', 'error': result.stderr}
    return {'status': 'completed'}