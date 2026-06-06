from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def safe_run(command_parts: list, **kwargs):
        try:
            result = subprocess.run(command_parts, capture_output=True, text=True, check=True, **kwargs)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    if host.strip() == '':
        return {'status': 'failed', 'error': 'Invalid host'}
    command_parts = ['ping', '-c', '1'] + shlex.split(host)
    return SafeSubprocess.safe_run(command_parts)