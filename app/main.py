from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Unauthorized access'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)