from fastapi import FastAPI
import subprocess

def validate_host(host):
    if '.' in host and not any(c.isalpha() for c in host) and all(c.isdigit() or c == '.' for c in host):
        return True
    return False

generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(generate_ping_command(host))
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400