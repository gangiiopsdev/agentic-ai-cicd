from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid hostname')
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    return SafeSubprocess.ping(host)