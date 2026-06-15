from fastapi import FastAPI
import subprocess
import shlex

class CommandSanitizer:
    @staticmethod
def sanitize(command: list) -> list:
        return [shlex.quote(arg) for arg in command]

app = FastAPI()

def safe_subprocess(command: list):
    try:
        result = subprocess.run(CommandSanitizer.sanitize(command), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', shlex.quote(host)]
    output = safe_subprocess(command)
    return {'status': 'completed', 'output': output}