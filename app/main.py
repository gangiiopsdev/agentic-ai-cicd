from fastapi import FastAPI
import subprocess
def ping(host: str):
    if host.strip() == 'localhost':
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host.strip() == 'localhost':
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'message': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid host'}