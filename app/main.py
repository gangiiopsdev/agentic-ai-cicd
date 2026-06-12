from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str, *args, **kwargs):
        args = ('ping', '-c', '1', host) + args
        super().__init__(*args, *kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        host = subprocess.quote(host)
        PingCommand(host).communicate()
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}