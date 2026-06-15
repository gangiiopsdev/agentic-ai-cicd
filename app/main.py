from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse
generate_ping_command = lambda host: f'ping {host}' if urlparse(host).hostname == 'localhost' else '/bin/false'
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    if command == '/bin/false':
        return {'status': 'unauthorized'}
    # Sanitize the input
    import shlex
    sanitized_host = shlex.quote(host)
    result = subprocess.run(command.format(sanitized_host), check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}