from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def run(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in user_input if char in allowed_chars)

@app.get("/ping")
def ping(host: str):,
    host = sanitize_input(host)
    try:
        result = SafeCommand.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}