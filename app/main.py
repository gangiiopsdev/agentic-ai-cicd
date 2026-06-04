from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        try:
            args = shlex.split(f'ping {host}')
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}