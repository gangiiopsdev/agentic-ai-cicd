from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host: str):
        try:
            return subprocess.check_output(['ping', host], universal_newlines=True)
        except subprocess.CalledProcessError as e:
            return f'Ping failed with error: {e}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return PingCommand.safe_ping(host)