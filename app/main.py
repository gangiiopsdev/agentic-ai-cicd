from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            output = subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': output.stdout}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    return SafePing.ping(host)