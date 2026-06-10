from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    return ['ping', '-c', '4', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}