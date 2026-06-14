from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    command = PingCommand(host)
    try:
        status = command.execute()
        return {'status': 'completed', 'output': status}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
def validate_host(host: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None