from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    validated_host = validate_host(host)
    if not validated_host:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', shlex.quote(validated_host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}