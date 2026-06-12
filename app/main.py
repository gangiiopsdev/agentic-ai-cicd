from fastapi import FastAPI
import subprocess
def generate_ping_command(host): return f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500