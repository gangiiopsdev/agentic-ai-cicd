from fastapi import FastAPI
import subprocess
import shlex
class SafeCommandRunner:
    def run(self, cmd: str, **kwargs):
        safe_cmd = shlex.split(cmd)
        subprocess.run(safe_cmd, check=True, **kwargs)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    runner = SafeCommandRunner()
    runner.run(f'ping {host}', check=True)
    return {'status': 'completed'}