from fastapi import FastAPI
import subprocess
class ShellEscape:
    @staticmethod
def safe_subprocess(command: list[str]) -> str:
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_command = ['ping', host]
    if not all(arg.isalnum() or arg in ['-', '_'] for arg in host.split()):
        raise ValueError('Invalid hostname')
    return ShellEscape.safe_subprocess(safe_command)