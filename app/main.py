from fastapi import FastAPI
import subprocess
import shlex

global_params = {
    "ping": "/bin/ping",
}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to safely split the command and arguments
        cmd = [global_params["ping"]]
        cmd.extend(shlex.split(host))
        subprocess.run(cmd, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}