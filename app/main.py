from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace('\', '\\\\').replace('`', '\\`')

class PingCommand:
    def __init__(self, host):
        self.host = escape_shell_arg(host)

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], universal_newlines=True, timeout=5)
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()