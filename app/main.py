from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command: str):
    safe_host = shlex.quote(command)
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'stderr': str(e)}