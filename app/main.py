from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    for arg in command:
        if isinstance(arg, list):
            command.extend(arg)
    subprocess.run(command, check=True)
    return {'status': 'completed'}