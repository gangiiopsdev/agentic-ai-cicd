from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = generate_ping_command(host)
    result = subprocess.run(command, capture_output=True, shell=False, text=True)
    return {'status': 'completed', 'output': result.stdout}