from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    def __init__(self, *args):
        self.args = args

    def run(self):
        safe_args = [shlex.quote(arg) for arg in self.args]
        command = ['ping'] + safe_args
        subprocess.run(command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = SafeCommand(host)
    safe_command.run()
    return {'status': 'completed'}