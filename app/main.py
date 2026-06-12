from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if host.startswith('127.0.0.1') or host.startswith('localhost') or '.' not in host.split(':')[0]:
            return {'status': 'completed', 'output': ''}
        else:
            try:
                output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
                return {'status': 'completed', 'output': output.stdout}
            except subprocess.CalledProcessError as e:
                return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return SafePing.safe_ping(host)