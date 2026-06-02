from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        try:
            args = ['ping', host]
            result = subprocess.run(shlex.split(' '.join(args)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

def ping_endpoint(host: str):
    return SafePing.ping(host)