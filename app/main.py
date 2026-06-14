from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation with shell=False and argument list
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}