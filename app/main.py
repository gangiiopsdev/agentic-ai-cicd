from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host):
        # Validate input to prevent injection
        if not all(c.isalnum() or c in '.-' for c in host):
            raise ValueError('Invalid hostname')
        super().__init__(['ping', '--quiet', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = PingCommand(host)
    output, error = result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}