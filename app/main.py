from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', subprocess.DEVNULL], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing(host)
    return safe_ping.ping()