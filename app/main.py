from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if 'ping' in host or '--help' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = subprocess.run(['ping', '-c', 1, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)

# Preventive Controls
# 1. Validate and sanitize all user inputs using a whitelist approach.
# 2. Use parameterized queries or similar constructs for database interactions to prevent SQL injection.
# 3. Implement proper logging and monitoring of system calls to detect suspicious activity.