from fastapi import FastAPI
import subprocess
def generate_ping_command(host):
    return ['ping', '-c', '4', host]
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious commands
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    command = generate_ping_command(host)
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}