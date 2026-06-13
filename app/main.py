from fastapi import FastAPI
import subprocess

def safe_ping(host):
    try:
        # Use a whitelist of allowed hosts or implement more robust validation
        allowed_hosts = ['example.com', 'another.example.com']
        if host not in allowed_hosts:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid host format')
    return safe_ping(host)