from fastapi import FastAPI
import subprocess
import shlex
class SafeProcess:
    @staticmethod
def safe_ping(host: str):
        ping_command = ['ping', host]
        try:
            result = subprocess.run(ping_command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafeProcess.safe_ping(host)