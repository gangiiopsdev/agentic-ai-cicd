from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Safely constructing the command without shell=True and validating input
        if host.strip() and not any(char in host for char in ['; ', '&', '|', '`']):
            args = ['ping', host]
            subprocess.run(args)
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)
    return {'status': 'completed'}