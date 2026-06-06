from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    try:
        command = ['ping', host]
        command_str = ' '.join(shlex.quote(arg) for arg in command)
        subprocess.run(command_str, shell=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}