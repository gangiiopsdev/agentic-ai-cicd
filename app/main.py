from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    def __init__(self):
        self.allowed_commands = ['ping']

    def execute(self, command, host):
        if command in self.allowed_commands:
            return subprocess.check_output([command, host], stderr=subprocess.STDOUT, timeout=10)
        else:
            raise ValueError('Command not allowed')

app = FastAPI()
safe_subprocess = SafeSubprocess()
@app.get('/ping')
def ping(host: str):
    try:
        output = safe_subprocess.execute('ping', host)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}