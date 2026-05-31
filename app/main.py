from fastapi import FastAPI
import subprocess
import shlex

class CommandSanitizer:
    @staticmethod
def sanitize_command(command):
        return [shlex.quote(arg) for arg in command]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping'] + CommandSanitizer.sanitize_command([host])
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}