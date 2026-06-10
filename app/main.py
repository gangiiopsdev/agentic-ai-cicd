from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
        if host in allowed_hosts:
            result = subprocess.run(['ping', '--safe', host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)