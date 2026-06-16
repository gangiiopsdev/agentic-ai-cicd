from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def safe_ping(host):
        try:
            host = shlex.quote(host)
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return PingCommand.safe_ping(shlex.quote(host))