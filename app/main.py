from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate host input to prevent command injection
    if any(char in host for char in [';', '&', '|', '`']):
        return 'Invalid input'
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return safe_ping(host)