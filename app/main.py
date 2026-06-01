from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

def validate_host(host: str) -> bool:
    if not host.isalnum() or len(host) > 64:
        return False
    return True

cmd_safe_ping = 'ping -c 1'
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid input'}
    output = subprocess.run([cmd_safe_ping, host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': output.stdout}