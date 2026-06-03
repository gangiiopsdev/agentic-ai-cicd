from fastapi import FastAPI
import subprocess
def generate_ping_command(host):\n    if not host or not isinstance(host, str) or not all(c.isalnum() or c in '-.' for c in host):\n        raise ValueError('Invalid host')\n    return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():\n    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):\n    try:\n        subprocess.call(generate_ping_command(host), shell=False)\n        return {'status': 'completed'}\n    except ValueError as e:\n        return {'error': str(e)}