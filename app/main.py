from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_endpoint(host: str):
    ping_instance = Ping(host)
    return {'status': 'completed', 'output': ping(host)}