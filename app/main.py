from fastapi import FastAPI
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        cmd = ['ping', shlex.quote(host)]
        return subprocess.run(cmd, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = PingService.ping(host)
    return {'status': 'completed', 'output': result.stdout}