from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command):
        # Ensure the command is safe
        allowed_commands = ['ping']
        if command in allowed_commands:
            subprocess.call(command)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    SafeSubprocess.call(['ping', host])
    return {'status': 'completed'}