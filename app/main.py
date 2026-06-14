from fastapi import FastAPI
import subprocess

generate_ping_command = lambda host: f'ping -c 4 {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(generate_ping_command(host), shell=False, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}