from fastapi import FastAPI
import subprocess
import shlex
def run_command(command: str):
    safe_command = shlex.split(shlex.quote(command))
    result = subprocess.run(safe_command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    try:
        # Use a safer alternative like using a library designed for network operations
        result = run_command(f'ping {host}')
        return result
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}