from fastapi import FastAPI
import subprocess
class ShellEscape:
    @staticmethod
def escape(command: str) -> str:
        return ' '.join([arg.replace(' ', '\ ') for arg in command.split()])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        escaped_host = ShellEscape.escape(host)
        output = subprocess.check_output(['ping', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}