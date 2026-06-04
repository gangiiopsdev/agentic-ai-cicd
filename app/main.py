from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input
        if not all(c.isalnum() or c in '.-:' for c in host):
            raise ValueError('Invalid host format')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    # Use a whitelist of allowed hosts instead of direct input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    return SafeSubprocess.ping(host)