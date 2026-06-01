from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if 'localhost' in host else None

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host or not host.isalnum() or 'localhost' not in host:
        return {'error': 'Invalid host'}, 400
    command = generate_ping_command(host)
    if command is not None:
        subprocess.call(command, shell=False)
    return {'status': 'completed'}