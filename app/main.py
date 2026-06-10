from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace('`', '\`').replace('$', '\$')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', '--'] + list(escape_shell_arg(host).split()), check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}