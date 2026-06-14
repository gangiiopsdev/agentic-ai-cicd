from fastapi import FastAPI
import subprocess
class SafePinger:
    @staticmethod
def safe_ping(host: str):
        # Validate the host input to ensure it only contains allowed characters
        if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
            raise ValueError("Invalid host name")
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

global pinger
pinger = SafePinger()

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = pinger.safe_ping(host)
    return {'status': 'completed', 'output': output}