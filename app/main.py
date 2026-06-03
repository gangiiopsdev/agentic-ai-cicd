from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        ip_parts = host.split('.')
        if len(ip_parts) != 4 or not all(part.isnumeric() and 0 <= int(part) <= 255 for part in ip_parts):
            raise ValueError('Invalid IP address')
        command = PingCommand(host)
        output = command.execute()
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}