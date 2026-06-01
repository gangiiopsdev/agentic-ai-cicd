from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        return subprocess.run(command, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = ['ping', host]
    result = SafeSubprocess.safe_run(command)
    return {'stdout': result.stdout.decode()}