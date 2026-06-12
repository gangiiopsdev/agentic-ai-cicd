from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using subprocess.run with shell=False and args parameter
        try:
            subprocess.run(['ping', host], check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    result = SafePing.ping(host)
    if result:
        return {'status': 'completed', 'output': result}
    else:
        return {'status': 'failed'}