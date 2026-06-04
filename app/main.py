from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    def __init__(self, command):
        self.command = command
        self.args = shlex.split(command)

    def run(self):
        result = subprocess.run(self.args, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e.isdigit() or e in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    safe_command = SafeCommand(command)
    output = safe_command.run()
    return {'status': 'completed', 'output': output}