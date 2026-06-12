from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        # Using shell=False for security and shlex.split to safely parse the command
        parts = shlex.split(command)
        result = subprocess.run(parts, capture_output=True, text=True, check=True, *args, **kwargs)
        return result.stdout
class SafePing:
    @staticmethod
def ping(host: str):
        # Validate host input here
        allowed_hosts = ['example.com', 'test.com']  # Example validation logic
        if host not in allowed_hosts:
            raise ValueError('Invalid host')
        return SafeSubprocess.run(f'ping {host}')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = SafePing.ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}, 400