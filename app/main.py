from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping 127.0.0.1' # Replace with a safe payload or method

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call([generate_random_payload, host], shell=False)
    return {'status': 'completed'}