from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_executable(executable):
    return executable.split()[0]

@app.get("/ping")
def ping(host: str):
    if 'ping' not in host or ';' in host or '&' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    return {'status': 'completed'}