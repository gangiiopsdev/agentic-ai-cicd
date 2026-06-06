from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Secure implementation using subprocess.run with shell=False and check=True for error handling
        args = ['ping', '-c', '1', host]
        try:
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return {'output': result.stdout, 'error': ''}
        except subprocess.CalledProcessError as e:
            return {'output': '', 'error': e.stderr}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    # Validate the input to prevent command injection
    if not host.strip() or any(char in host for char in [';', '&', '|', '<', '>', '*', '?', '~', '`']):
        return {'error': 'Invalid input'}
    return SafePing.ping(host)