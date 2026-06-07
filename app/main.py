from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Sanitize input by escaping special characters
        escaped_host = host.replace('\', '/').replace(';', '')
        output = subprocess.check_output(['ping', '-c', '1', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)