from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr.strip()}'

app = FastAPI()

@app.get("/ping")
def ping_secure(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}