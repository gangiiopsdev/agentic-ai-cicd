from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: list, capture_output=True, text=True, check=True):
        try:
            result = subprocess.run(command, capture_output=capture_output, text=text, check=check)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise e

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    output = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': output}