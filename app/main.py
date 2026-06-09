from fastapi import FastAPI
import subprocess
import shlex
from shlex import quote as cmd_quote

class PingService:
    @staticmethod
def ping(host: str) -> dict:
        try:
            output = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return PingService.ping(host)