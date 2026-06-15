from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_hosts = {'localhost', '127.0.0.1'}
    return host.strip() if host in allowed_hosts else None

def safe_ping(host: str) -> bool:
    allowed_commands = ['ping', '-c 4']
    command = allowed_commands + [host]
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr.decode()}')
        return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        if safe_ping(sanitized_host):
            return {'status': 'completed'}
        else:
            return {'error': 'Ping failed'}
    else:
        return {'error': 'Invalid host'}