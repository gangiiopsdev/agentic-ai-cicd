from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a whitelist of allowed hosts or implement more robust validation
        if host not in ['example.com', 'another.example.com']:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
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