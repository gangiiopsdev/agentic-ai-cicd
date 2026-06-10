from fastapi import FastAPI
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

app = FastAPI()
def ping(host: str):
    try:
        result = subprocess.run(['ping', PingCommand(host).host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}