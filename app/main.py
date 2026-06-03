from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = ['ping', *shlex.split(host)]
    output = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}
class SafeSubprocessWrapper:
    def __init__(self, command):
        self.command = command

    def run(self):
        try:
            output = subprocess.run(self.command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_subprocess = SafeSubprocessWrapper(['ping', *shlex.split(host)])
    return safe_subprocess.run()