from fastapi import FastAPI
import subprocess
import shlex

gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it's a valid hostname or IP address
    if not validate_host(host):
        return {'error': 'Invalid host provided'}
    try:
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

def validate_host(host: str) -> bool:
    import socket
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False