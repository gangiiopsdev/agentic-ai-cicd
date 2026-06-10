from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: f'ping {quote(host)}'

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    command = generate_ping_command(host)
    args = command.split(' ')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed'}