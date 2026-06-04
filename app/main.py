from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str):
        super().__init__(args=['ping', host], shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    command.wait()
    return {'status': 'completed'}