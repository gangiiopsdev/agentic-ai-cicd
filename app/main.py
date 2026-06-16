from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_run(command, *args):
        try:
            result = subprocess.run(command, args=args, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in '.-@' for c in host):
        raise ValueError('Invalid hostname')
    safe_command = shlex.split(f'ping -c 1 {host}')
    return {'status': 'completed', 'output': SafeSubprocess.safe_run(safe_command)}