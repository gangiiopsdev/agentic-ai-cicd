from fastapi import FastAPI
import subprocess
import shlex
class Ping:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]  # Remove shlex.quote to avoid potential shell injection
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    return {'status': 'completed', 'result': ping_instance.execute()}