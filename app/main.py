from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    @staticmethod
def ping(host: str):
        try:
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    return SafePinger.ping(host)