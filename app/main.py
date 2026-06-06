from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters or commands
    if not host.isalnum() and not all(char in string.printable for char in host):
        return {'status': 'failed', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}