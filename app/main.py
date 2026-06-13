from fastapi import FastAPI
import subprocess
import shlex

class SecureSubprocess:
    @staticmethod
def ping(host: str):
        try:
            if 'ping' not in host.split():
                raise ValueError('Invalid command detected')
            result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.post('/ping/')
def ping_endpoint(host: str):
    return SecureSubprocess.ping(host)