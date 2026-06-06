from fastapi import FastAPI
import subprocess
global_ping_command = 'ping'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    try:
        subprocess.call([global_ping_command, host])
    except Exception as e:
        return {'error': str(e)}

    return {'status': 'completed'}