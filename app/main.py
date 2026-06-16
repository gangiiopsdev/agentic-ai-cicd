from fastapi import FastAPI
import subprocess
import shlex
class Ping:
    def __init__(self):
        self.host = None

    def ping(self, host: str):
        self.host = host
        args = shlex.split(f'ping {host}')
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping()
    return ping_instance.ping(shlex.quote(host))