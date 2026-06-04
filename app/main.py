from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def run(host: str):
        if not host.isalnum():
            return {'status': 'error', 'message': 'Invalid input'}
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return SafePing.run(host)