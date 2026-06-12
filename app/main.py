from fastapi import FastAPI
import subprocess
generate_ping_command = ['ping', '-c', '1']
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(generate_ping_command + [host], check=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
def validate_host(host: str) -> bool:
    # Stronger validation logic to check if the host is safe
    allowed_hosts = ['google.com', 'example.com']
    return all([char.isalnum() or char in ['.','-','_'] for char in host]) and len(host.split('.')) == 2