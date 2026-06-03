from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', '-c', '1', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.check_call(generate_ping_command(host), stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}