from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def call(command, **kwargs):
        return subprocess.call(subprocess.list2cmdline(command.split()), **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        SafeSubprocess.call(['ping', host])
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}