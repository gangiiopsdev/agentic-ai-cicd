from fastapi import FastAPI
import subprocess
def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not all(char.isalnum() or char in ['.', '-'] for char in host):
        return {'error': 'Invalid host'}
    command = ['ping', host]
    return {'status': execute_command(command)}