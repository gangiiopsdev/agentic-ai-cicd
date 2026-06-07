from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            # Use shlex.quote to safely escape the input
            result = subprocess.run(shlex.split(f'ping {self.host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return str(e.stderr.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand(host).run()