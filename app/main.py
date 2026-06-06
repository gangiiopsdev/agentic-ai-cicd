from fastapi import FastAPI
import subprocess

def escape_command(command):
    return [arg.strip() for arg in command.split()]  # Use a list of arguments instead of a single string

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    subprocess.run(command, check=True)  # Use subprocess.run for better error handling and security
    return {'status': 'completed'}