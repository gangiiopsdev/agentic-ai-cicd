from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        # Use shlex to safely escape arguments
        args = ['ping'] + shlex.split(host)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}