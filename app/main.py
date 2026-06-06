from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            args = shlex.split('ping') + [self.host]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output).decode('utf-8')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist
    return True