from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['-', '.', '_', ':', '/', '@', '!'])

class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        try:
            subprocess.run(command, check=True, **kwargs)
        except subprocess.CalledProcessError as e:
            raise Exception(f'Command failed: {e}')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    SafeSubprocess.run(['ping', sanitized_host])
    return {'status': 'completed'}