from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', *shlex.split(self.host)], check=True, stdout=subprocess.PIPE)
            return output.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it with subprocess
    if not host or not host.isalnum():
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(shlex.quote(host))
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}