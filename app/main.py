from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run for a safer alternative
        result = subprocess.run(['ping', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e}')
        return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host.strip()):  # Strip any leading/trailing whitespace
        return {'status': 'completed', 'result': 'Ping successful'}
    else:
        return {'status': 'failed', 'result': 'Ping failed'}