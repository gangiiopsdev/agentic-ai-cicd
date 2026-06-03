from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def run_ping(host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    result = SafePing.run_ping(host)
    return {'status': 'completed', 'output': result}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)