from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Use subprocess.run instead of subprocess.call with shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}