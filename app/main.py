from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def escape_shell_argument(value):
        return value.replace(';', ' ').replace('&', ' ').replace('|', ' ')

app = FastAPI()

def ping(host: str):
    try:
        args = shlex.split(f'ping {PingCommand.escape_shell_argument(host)}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum():  # Simplified validation
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)