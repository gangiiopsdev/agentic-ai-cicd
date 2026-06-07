from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    @staticmethod
def ping(host: str):
        # Validate the host input to prevent command injection
        if not host.replace('.', '').isnumeric() or '@' in host:
            raise ValueError('Invalid host format')
        try:
            cmd = ['ping', '-c', '1'] + shlex.split(host)
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return SafeCommandRunner.ping(host)