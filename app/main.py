from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    return PingCommand.run(host)