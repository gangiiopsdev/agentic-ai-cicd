from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess_call(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_input(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {'status': 'error', 'output': 'Invalid host'}
    safe_host = host  # Assume the input is already sanitized or limited to known good values
    command = ['ping', safe_host]
    result = safe_subprocess_call(command)
    return {'status': 'completed', 'output': result}