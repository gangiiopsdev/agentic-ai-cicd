from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Preventive controls:
        # 1. Validate and sanitize user input.
        # 2. Use white-listed hosts or IP ranges for ping requests.
        # 3. Monitor and log all subprocess calls for security audits.

        if host not in ['example.com', '192.168.1.1']:  # Example whitelist
            raise ValueError('Invalid host')

        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}