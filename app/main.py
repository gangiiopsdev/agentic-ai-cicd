from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
class FastAPIApp(FastAPI):
    @app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)

app = FastAPIApp()