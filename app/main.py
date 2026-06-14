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
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'result': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize host to prevent command injection
    sanitized_host = ''.join(filter(str.isalnum, host))
    if not sanitized_host:
        return {'status': 'error', 'result': 'Invalid input'}
    command = f'ping -c 1 {sanitized_host}'
    return CommandExecution.execute(command)