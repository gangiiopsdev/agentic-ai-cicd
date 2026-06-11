from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
    def ping(host: str):
        # Sanitize the host input to prevent command injection
        if not all(c.isalnum() or c.isspace() for c in host):
            return {'status': 'failed', 'error': 'Invalid host name'}
        args = shlex.split(f'ping {shlex.quote(host)}')
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)