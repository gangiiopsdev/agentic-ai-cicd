from fastapi import FastAPI
import subprocess
def ping(host: str):
    sanitized_host = host.strip().replace(';', '').replace('&', '')
    # Use a safe method instead of subprocess.run
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)