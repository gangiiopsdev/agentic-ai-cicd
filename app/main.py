from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
class SafePingCommand:
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        try:
            result = subprocess.run(self.command, shell=False, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr
class SafePingHost:
    def __init__(self, host: str):
        self.host = host

    def is_safe_host(self):
        return all(c.isalnum() or c in ['.', '-'] for c in self.host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = SafePingHost(host)
    if not safe_host.is_safe_host():
        raise ValueError('Invalid host name')
    safe_command = SafePingCommand(f'ping {host}')
    output = safe_command.execute()
    return {'status': 'completed', 'output': output}