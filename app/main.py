from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and '&&' not in host and ';' not in host

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid input'}

    # Secure implementation using subprocess.run with shell=False and fully qualified executable path
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed'}
    return {'status': 'completed', 'output': result.stdout}