from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not host.isdigit():
            return {'status': 'error', 'message': 'Invalid input'}
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    try:
        return SafePing.ping(host)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}