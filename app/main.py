from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Use a safe alternative to subprocess for the specific task of pinging
        output = subprocess.run(['ping', '-c', '4', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}