from fastapi import FastAPI
import subprocess
class SafePing:
    def __call__(self, host: str):
        safe_host = subprocess.quote(host)
        return subprocess.call(f'ping {safe_host}', shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}