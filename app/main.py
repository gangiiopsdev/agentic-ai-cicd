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
    args = ['ping'] + CommandSanitizer.sanitize_command([host])
    # Use subprocess.run instead of subprocess.call to avoid shell=True and potential RCE
    subprocess.run(args, check=True)
    return {'status': 'completed'}