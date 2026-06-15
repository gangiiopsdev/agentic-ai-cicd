from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host):
        try:
            result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode()
        except Exception as e:
            return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    return {'status': 'completed', 'output': safe_ping(host)}