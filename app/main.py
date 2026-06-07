from fastapi import FastAPI
import subprocess
import shlex
def run_command(command: str, args: List[str]) -> subprocess.CompletedProcess:
    cmd = [command]
    for arg in args:
        cmd.append(shlex.quote(arg))
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = run_command('/bin/ping', [shlex.quote(host)])  # Ensure host is a list to avoid shell injection risks
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}