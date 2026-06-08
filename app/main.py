from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> dict:
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return PingCommand(host).execute()