from fastapi import FastAPI
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', shlex.quote(self.host)]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_instance = Ping(host)
    return {'status': 'completed', 'result': ping_instance.execute()}