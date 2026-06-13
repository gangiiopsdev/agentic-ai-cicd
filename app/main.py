from fastapi import FastAPI
import subprocess
global_config = {'ping_command': 'ping'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = [global_config['ping_command'], host]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}