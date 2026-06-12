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
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}