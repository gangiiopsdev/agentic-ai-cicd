from fastapi import FastAPI
import subprocess
def sanitize_input(host):
    allowed_hosts = ['example.com', 'localhost']  # Define allowed hosts
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host is not None:
        try:
            result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}, 500
    else:
        return {'status': 'invalid host'}, 400