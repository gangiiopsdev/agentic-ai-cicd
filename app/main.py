from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate host input to ensure it's a safe target for pinging
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'error': 'Invalid hostname'}
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

# Import re module for regular expression matching
import re