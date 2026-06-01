from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        pass

    def safe_ping(self, host):
        try:
            command = ['ping', '-c', '1', shlex.quote(host)]
            output = subprocess.check_output(command, stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()
dp = SafePing()

@app.get("/ping")
def ping(host: str):
    return dp.safe_ping(host)