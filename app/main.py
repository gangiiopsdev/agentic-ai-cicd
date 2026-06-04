from fastapi import FastAPI
import subprocess
import shlex
class SafeCommand:
    @staticmethod
def ping(host: str):
        allowed_hosts = ['localhost', '127.0.0.1']  # Add allowed hosts here
        if host in allowed_hosts:
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            return {'status': 'error', 'message': 'Invalid host'}

app = FastAPI()

@app.get('/ping')
def ping_wrapper(host: str):
    return SafeCommand.ping(host)