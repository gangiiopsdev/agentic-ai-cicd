from fastapi import FastAPI
import subprocess
class CommandWrapper:
    def __init__(self, command):
        self.command = command.split()

    def execute(self):
        try:
            output = subprocess.check_output(self.command, stderr=subprocess.STDOUT)
            return output.decode().strip()
        except subprocess.CalledProcessError as e:
            return e.output.decode().strip()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or len(host) > 255 or '\' in host:
        raise ValueError('Invalid host')
    wrapper = CommandWrapper(['ping', host])
    return {'status': 'completed', 'output': wrapper.execute()}