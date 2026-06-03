from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Safely constructing the command without shell=True and validating input
        if host.strip() and not any(char in host for char in ['; ', '&', '|', '`']):
            args = ['ping', '-c 4', host]
            subprocess.run(args, check=True)
app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing.safe_ping(host)
    return {'status': 'completed'}