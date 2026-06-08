from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def ping(host: str):
        if 'ping' in host:
            return {'error': 'Invalid hostname'}
        try:
            output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    result = SafePinger.ping(host)
    return result