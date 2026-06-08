from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure the host parameter only contains valid characters
        if all(c.isalnum() or c in ('.', '-', '_') for c in host):
            subprocess.call(['ping', host])
        else:
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}