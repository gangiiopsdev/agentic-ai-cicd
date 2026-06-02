from fastapi import FastAPI
import subprocess
def validate_input(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_input(host):
        return {'status': 'error', 'output': 'Invalid host'}
    command = ['ping', host]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return str(e)