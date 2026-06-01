from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Using subprocess.run with shlex.split to avoid shell=True and potential injection attacks
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)