from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host
        self.args = ['ping', self.host]
@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 50:
        return {'status': 'invalid input'}, 400
    try:
        result = subprocess.run(shlex.split(' '.join(ping_command.args)), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}, 500