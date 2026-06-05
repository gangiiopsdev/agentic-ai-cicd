from fastapi import FastAPI
import subprocess
def escape_command(command):
    return [arg.strip() for arg in command.split()]

def safe_ping(host: str):
    valid_hosts = ['example.com', 'test.net']
    if host not in valid_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ['example.com', 'test.net']:
        return {'error': 'Invalid host'}
    try:
        subprocess.run(escape_command(f'ping {host}'), check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}
    return {'status': 'completed'}