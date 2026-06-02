from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with input validation
    allowed_hosts = ['127.0.0.1', '::1']  # List of allowed hosts
    if host in allowed_hosts:
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': result.stdout}
    else:
        return {'error': 'Host not allowed'}, 403