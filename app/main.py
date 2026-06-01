from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Safe implementation
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input further to prevent shell injection
    if not host.isalnum() or '>' in host or '<' in host or '&' in host or '|' in host or ';' in host:
        return {'status': 'error', 'result': 'Invalid input'}
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}