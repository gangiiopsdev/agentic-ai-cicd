from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    if not host.strip().isdigit() or '.' not in host:
        raise ValueError('Invalid host format')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        safe_command = ['ping', host]
        output = run_safe_command(safe_command)
        return {'status': 'completed' if not output.startswith('ping:') else 'error', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}