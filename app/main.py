from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.ping_path = '/bin/ping'

    def ping(self, host: str):
        try:
            result = subprocess.run([self.ping_path, '-c', '1', host], check=True, stdout=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()
ping_command = PingCommand()

@app.get("/ping")
def ping_route(host: str):
    return ping_command.ping(host)