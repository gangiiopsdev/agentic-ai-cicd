from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    if not host or not isinstance(host, str) or not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host')
    return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = generate_ping_command(host)
        subprocess.run(command.split(), check=True)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}