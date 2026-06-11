from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = ['ping', 'localhost']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    ping_instance = PingCommand()
    subprocess.call(ping_instance.command)

    return {'status': 'completed'}