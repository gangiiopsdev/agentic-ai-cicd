from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = ['ping', host]
            subprocess.run(args, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    return SafePing.ping(host)