from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    command = ['ping', host]
    try:
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)