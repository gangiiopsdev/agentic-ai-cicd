from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Use os.system or subprocess.run with shell=False for safer execution
    command = ['ping', host]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)