from fastapi import FastAPI
import subprocess
def run_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a valid host
    if not is_valid_host(host):
        return {'status': 'invalid', 'error': 'Invalid host'}
    return run_ping(host)

def is_valid_host(host: str) -> bool:
    import socket
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False