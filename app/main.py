from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        if not host.isdigit():
            return {'status': 'error', 'message': 'Invalid input'}
        command = ['ping', '-c', '1', host]  # Limit the number of pings to avoid potential DoS
        result = subprocess.run(command, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return SafePing.ping(host)