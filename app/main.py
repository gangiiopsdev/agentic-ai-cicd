from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
        return subprocess.run(command, check=True, capture_output=True, text=True, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', '-c', '1', host]
    result = SafeSubprocess.run(command)
    return {'status': 'completed', 'output': result.stdout}