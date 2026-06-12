from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        if host == 'localhost':
            return subprocess.call(['ping', '-c', '1', host])
        else:
            raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        PingCommand.run(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400