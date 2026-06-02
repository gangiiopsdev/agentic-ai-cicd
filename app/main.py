from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Ensure host is safe by validating it against expected formats
        if not host or '@' in host or '/' in host:
            raise ValueError('Invalid host input')
        command = ['ping', host]
        subprocess.run(command, check=True)
app = FastAPI()
@app.get('/'
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}