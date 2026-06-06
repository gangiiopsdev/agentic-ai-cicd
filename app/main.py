from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ['-', '.', '/', ':', '@'])

class SafeSubprocess:
    @staticmethod
def run_command(command, *args, **kwargs):
        sanitized_args = [arg.replace('--', '').replace(';', '') for arg in args]
        return subprocess.run([command, *sanitized_args], capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    result = SafeSubprocess.run_command('ping', *shlex.split(sanitized_host))
    return {'status': 'completed', 'output': result.stdout}