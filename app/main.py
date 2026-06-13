from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Sanitize host input using a whitelist of allowed hosts
        allowed_hosts = ['example.com', 'localhost']
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.output.decode('utf-8')}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)