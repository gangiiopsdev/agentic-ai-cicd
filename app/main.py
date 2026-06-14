from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_safe_command(command, args):
    full_command = [command] + args
    subprocess.run(full_command, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    execute_safe_command('ping', [host])
    return {'status': 'completed'}