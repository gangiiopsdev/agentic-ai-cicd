from fastapi import FastAPI
import subprocess
global_vars = {'__builtins__': None}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}