from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-', '_', ''])
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = shlex.split(f'ping {shlex.quote(self.host)}')
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(str(e))

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = PingCommand(sanitized_host)
    try:
        command.execute()
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}