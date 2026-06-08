from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        if not isinstance(command, str) or not all(isinstance(arg, str) for arg in args):
            raise ValueError('Command and arguments must be strings')
        safe_command = shlex.split(command)
        return subprocess.run(safe_command, capture_output=True, text=True, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Use SafeSubprocess for better security and control over the command execution
        result = SafeSubprocess.run(f'ping {host}')
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}