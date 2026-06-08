from fastapi import FastAPI
import subprocess
def secure_ping(host):
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        return secure_ping(host)
    else:
        return {'status': 'error', 'message': 'Invalid host'}

def is_valid_host(host):
    # Implement logic to validate the host input
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts