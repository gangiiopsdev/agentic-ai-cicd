from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if all(c.isalnum() or c in ('-', '.', '_') for c in host):  # Basic validation of the hostname
        try:
            subprocess.run(['ping', host], check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Invalid hostname'}, 400