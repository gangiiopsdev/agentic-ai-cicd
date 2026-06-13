from fastapi import FastAPI
import subprocess
class PingCommandRunner:
    @staticmethod
def run(host: str):
        args = ['ping', host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = PingCommandRunner.run(host)
    return {'status': result.stdout}