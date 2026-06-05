from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    return all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host)

def safe_ping(host: str) -> bytes:
    command = ['ping', '-c', '1', host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive Controls:
# - Use input validation to ensure the host parameter only contains allowed characters.
# - Avoid using shell=True in subprocess calls when possible.
# - Consider using a whitelist of allowed hosts.