from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid host name')
        subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    PingCommand.safe_ping(host)
    return {'status': 'completed'}