from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        sanitized_host = ''.join(c for c in self.host if c.isalnum() or c in ('.', '-'))
        args = shlex.split(f'ping {sanitized_host}')
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    return command.execute()