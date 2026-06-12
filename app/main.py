from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        command += ' '.join(args)
        return subprocess.call(command, shell=True, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(SafeSubprocess.call('ping', host), shell=True)
    return {'status': 'completed'}