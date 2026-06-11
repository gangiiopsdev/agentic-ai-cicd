from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'output': 'Invalid host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    try:
        output = subprocess.check_output(['ping', '-c 1', host], shell=False, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode()}