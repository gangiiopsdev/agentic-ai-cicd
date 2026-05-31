from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get('/ping/{host:path}')
def ping_route(host: str):
    try:
        ping_cmd = PingCommand(host)
        output = ping_cmd.run()
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}