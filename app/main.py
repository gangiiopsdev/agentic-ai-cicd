from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.run(['ping', '-c', '1'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed' if safe_ping(host) else 'failed'}
    except ValueError as e:
        return {'error': str(e)}, 400