from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if host in ['localhost', '127.0.0.1']:
            command = ['ping'] + shlex.split(host)
            subprocess.call(command, shell=False)
        return {'status': 'completed'}

app = FastAPI()

@app.get('/ping')
def ping_host(host: str):
    return SafeSubprocess.ping(host)