from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Safe implementation
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = execute_ping(host)
    if isinstance(response, dict) and 'error' in response:
        return response
    else:
        return {'status': 'completed'}