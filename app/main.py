from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.sanitized_commands = {
            'ping': ['ping', '-c', '1'],
            # Add more safe commands here as needed
        }

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = SafePing().sanitized_commands.get('ping', ['ping'])
    subprocess.call(safe_command + [host])
    return {'status': 'completed'}