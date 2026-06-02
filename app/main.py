from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        safe_host = escape_host(host)
        args = shlex.split(f'ping {safe_host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}