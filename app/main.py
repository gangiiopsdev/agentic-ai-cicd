from fastapi import FastAPI
import subprocess
import shlex
class CommandExecution:
    @staticmethod
def execute(command: str):
        # Validate command for allowed characters and length
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.:/\'
        if not all(char in allowed_chars for char in command):
            return {'status': 'error', 'result': 'Invalid command'}
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=False)  # Use check=False to handle errors manually
        if result.returncode != 0:
            return {'status': 'error', 'result': result.stderr}
        else:
            return {'status': 'completed', 'result': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = ''.join(filter(str.isalnum, host))
    command = f'ping {sanitized_host}'
    try:
        return CommandExecution.execute(command)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'result': str(e)}