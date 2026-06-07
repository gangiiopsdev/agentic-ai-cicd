from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
    output, error = process.communicate()
    if process.returncode != 0:
        raise Exception(f'Ping failed: {error}')

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.Popen to escape command arguments
    safe_ping(host)
    return {'status': 'completed'}