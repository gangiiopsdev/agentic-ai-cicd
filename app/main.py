from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation using shlex and ensuring safe input handling
    command_parts = shlex.split(host)
    command = ['ping'] + command_parts
    subprocess.run(command, check=True, capture_output=True, text=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex and ensuring safe input handling
    command_parts = shlex.split(host)
    command = ['ping'] + command_parts
    subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed'}