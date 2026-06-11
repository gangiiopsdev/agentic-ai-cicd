from fastapi import FastAPI
import subprocess
class SafeCommand:
    @staticmethod
def run(command, *args, **kwargs):
        return subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, *args, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = SafeCommand.run(['ping', host], timeout=5)
        return {'status': 'completed', 'output': output.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output.decode('utf-8'))}