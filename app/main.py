from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.list2cmdline([host])
    command = generate_ping_command(safe_host)
    subprocess.call(command, shell=False)
    return {'status': 'completed'}