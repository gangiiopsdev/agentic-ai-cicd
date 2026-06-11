from fastapi import FastAPI
import subprocess
import shlex

def generate_ping_command(host):
    return ['ping', '-c', '1', shlex.quote(host)]

def sanitize_input(user_input):
    # Basic sanitization: allow only alphanumeric characters and hyphens
    return ''.join(c for c in user_input if c.isalnum() or c == '-').replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(generate_ping_command(sanitized_host), check=True)
    return {'status': 'completed'}