from fastapi import FastAPI
import subprocess
def execute_safe_command(command, *args):
    safe_args = [subprocess.quote(arg) for arg in args]
    try:
        result = subprocess.run([command] + safe_args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

class SafePingCommand:
    def __init__(self, command='ping', *args):
        self.command = command
        self.args = args

    def execute(self, host):
        safe_host = subprocess.quote(host)
        result = self.execute_safe_command(self.command, safe_host)
        return {'status': 'completed', 'result': result}

global ping
ping = SafePingCommand()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping.execute(host)