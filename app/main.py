from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def call(host: str):
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = PingCommand.call(host)
    return {'status': 'completed', 'output': output}