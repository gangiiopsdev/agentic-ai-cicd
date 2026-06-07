from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode())

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic input validation
        return {'error': 'Invalid input'}, 400
    return {'status': safe_ping(host)}