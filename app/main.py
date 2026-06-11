from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['example.com', 'test.com']
    return host if host in allowed_hosts else ''

app = FastAPI()
def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode("utf-8")}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'output': 'Invalid host'}
    command_parts = ['ping', '--', sanitized_host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}