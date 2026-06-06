from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping'] + shlex.split(host)
        subprocess.call(args, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)