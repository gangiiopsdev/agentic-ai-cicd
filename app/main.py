from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str) -> dict:
        if 'ping' not in host:
            raise ValueError('Invalid input detected')
        args = ['ping'] + shlex.split(host)
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        return SafePing.safe_ping(host)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}