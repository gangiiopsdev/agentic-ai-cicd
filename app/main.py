from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        try:
            result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), check=True, capture_output=True)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not shlex.quote(host) == host:
        raise ValueError("Invalid characters in host parameter")
    return SafePing.safe_ping(host)