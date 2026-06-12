from fastapi import FastAPI
import subprocess
def shlex_split_safe(input_string):
    return [item for item in input_string.strip().split(' ') if item]
class PingService:
    @staticmethod
def ping(host: str):
        # Validate host to prevent command injection
        if not host.isalnum() or '.' not in host:
            raise ValueError('Invalid host')
        command = ['ping'] + shlex_split_safe(host)
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {'status': 'completed', 'output': result.stdout}