from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_shell_command(command_parts):
    if any(char in command_parts for char in [';', '&', '|', '>', '<', '*', '?', '{', '}', '~', '`']):
        raise ValueError('Unsafe characters detected in command input')

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {host}')
        secure_shell_command(args)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}