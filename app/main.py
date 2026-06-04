from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping' # Replace with a safe payload or method

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'error', 'message': 'Invalid host'}

    # Safe payload execution
    cmd = [generate_random_payload, '127.0.0.1']  # Use hardcoded safe input
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}

# Secure fix: Validate and sanitize user input before using it in subprocess calls.
def validate_and_sanitize(user_input):
    allowed_hosts = ['127.0.0.1', '::1']
    if user_input not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping_secure')
def ping_secure(host: str):
    try:
        validate_and_sanitize(host)
        cmd = [generate_random_payload, host]
        subprocess.run(cmd, check=True)
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}