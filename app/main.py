from fastapi import FastAPI
import subprocess

def safe_subprocess(command: list) -> str:
    try:
        output = subprocess.check_output(command, universal_newlines=True, timeout=5)
        return output.strip()
    except subprocess.CalledProcessError as e:
        raise Exception(f'Command failed with error {e}')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError('Invalid input for host parameter')
    command = ['ping', host]
    try:
        output = safe_subprocess(command)
        return {'status': 'completed', 'output': output}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}