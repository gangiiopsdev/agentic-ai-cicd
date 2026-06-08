from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = shlex.split(f'ping {host}')
            output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()
def ping_endpoint(host: str):
    try:
        SafePing.ping(host)
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}