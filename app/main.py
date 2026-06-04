from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)