from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit())

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'error': 'Host parameter is required'}
    # Secure implementation
    sanitized_host = sanitize_input(host)
    command = ['ping', '-c', '1', sanitized_host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e.stderr}'}