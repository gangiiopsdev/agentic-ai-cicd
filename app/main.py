from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host):
        super().__init__(args=['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_cmd = PingCommand(host)
    stdout, stderr = ping_cmd.communicate()
    return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode() if stderr else ''}