from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        command = ['ping'] + shlex.split(host)
        try:
            subprocess.run(command, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': e}

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    return SafeSubprocess.ping(host)