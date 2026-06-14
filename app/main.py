from fastapi import FastAPI
import subprocess

def safe_ping(host: str) -> dict:
    if not host or not host.strip().isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed: {error}')
    return {'status': 'completed', 'output': output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)