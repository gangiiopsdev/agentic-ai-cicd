from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Use the -c option to limit the number of pings and prevent potential DoS attacks
    return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    result = safe_ping(host)
    return {'status': 'completed', 'result': result.stdout}