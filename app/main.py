from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping': True}

    def ping(self, host: str):
        if 'ping' in host or any(command in host for command in self.safe_commands):
            raise ValueError('Unsafe command detected')
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping_route(host: str):
    return safe_ping.ping(host)