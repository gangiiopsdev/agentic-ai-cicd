from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_host(host: str):
    if not validate_input(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)

def validate_input(input_str: str) -> bool:
    # Implement proper validation logic here, e.g., regex patterns for allowed hostnames/IPs
    allowed_hosts = ['localhost', '127.0.0.1']
    return input_str in allowed_hosts