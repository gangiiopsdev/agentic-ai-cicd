from fastapi import FastAPI
import subprocess
getent = __import__('getent')

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    try:
        getent.hosts(host)
    except KeyError:
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)