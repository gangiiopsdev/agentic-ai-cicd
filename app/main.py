from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = generate_ping_command(host)
    args = ['ping'] + command.split()[1:]  # Avoid using shell=True and split the command manually
    subprocess.call(args)
    return {'status': 'completed'}