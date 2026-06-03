from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', f'--{host}'], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'
    else:
        return 'Host not allowed'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)