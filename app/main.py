from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if '@' in host or ';' in host or '|' in host or '&' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    # Sanitize the host input before passing to PingCommand
    sanitized_host = subprocess.quote(host)
    ping_command = PingCommand(sanitized_host)
    return ping_command.execute()