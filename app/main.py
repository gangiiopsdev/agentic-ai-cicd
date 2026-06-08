from fastapi import FastAPI
import subprocess

def generate_ping_command(host):
    return ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.run(generate_ping_command(host), check=True)
    return {'status': 'completed'}