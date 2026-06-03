from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        return {'status': 'completed', 'result': safe_ping(host)}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Add logic to validate the host parameter
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts