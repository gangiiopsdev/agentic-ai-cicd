from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run(command: list):
        try:
            result = subprocess.run(command, capture_output=True, check=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'result': result}