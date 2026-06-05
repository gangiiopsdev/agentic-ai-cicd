from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', 'example.com']

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to avoid command injection
    sanitized_host = ''.join(x if x.isalnum() or x in ('.', '-', '_') else '_' for x in host)
    SafePing().ping_command[1] = sanitized_host
    result = subprocess.run(SafePing().ping_command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}