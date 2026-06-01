from fastapi import FastAPI
import subprocess
import shlex

class App:
    def __init__(self):
        self.app = FastAPI()

    def home(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

    @app.get('/ping')
    def ping(host: str):
        if not host.isalnum() and '-' not in host:
            return {'status': 'failed', 'error': 'Invalid host parameter'}
        try:
            command = ['ping', shlex.quote(host)]
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr.decode())}