from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    @staticmethod
def run(host: str):
        if not host.isnumeric():
            raise ValueError('Invalid input')
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping_endpoint(host: str):
    try:
        return PingCommand.run(host)
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}