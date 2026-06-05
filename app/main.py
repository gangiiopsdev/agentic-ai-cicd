from fastapi import FastAPI
import subprocess
import shlex
def safe_shell(args):
    return ' '.join([shlex.quote(a) for a in args])
class SafeSubprocess:
    @staticmethod
def run(command: str):
        parts = shlex.split(safe_shell(command))
        try:
            result = subprocess.run(parts, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.stderr}'
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host or host.strip() == '':
        return {'status': 'error', 'output': 'Host parameter is required'}
    command = f'ping {host}'
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': result}