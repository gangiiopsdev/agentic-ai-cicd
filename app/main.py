from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        command = ['ping', host]
        args = ' '.join(shlex.quote(arg) for arg in command)
        output = subprocess.check_output(['sh', '-c', args], stderr=subprocess.STDOUT, shell=True)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e.output)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)