from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_ping(host):
        command = ['ping', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafeSubprocess.safe_ping(host)