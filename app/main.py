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
    sanitized_host = subprocess.list2cmdline([host])
    SafePing().ping_command[1] = sanitized_host
    subprocess.run(SafePing().ping_command, shell=False)
    return {'status': 'completed'}