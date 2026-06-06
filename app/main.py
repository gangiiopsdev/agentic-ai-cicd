from fastapi import FastAPI
import subprocess
import shlex
class SubprocessWrapper:
    def __init__(self):
        self.allowed_commands = ['ping']

    def run_command(self, command: str, args: list):
        if command not in self.allowed_commands:
            raise ValueError('Command not allowed')
        full_command = [command] + args
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
subprocess_wrapper = SubprocessWrapper()
def ping(host: str):
    try:
        result = subprocess_wrapper.run_command('ping', [host])
        return {'status': 'completed', 'output': result['output']}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return ping(host)