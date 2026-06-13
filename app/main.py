from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}

class PingEndpoint:
    def __init__(self):
        pass

    @app.get("/ping")
    def ping(self, host: str):
        ping_command = PingCommand(host)
        return {'status': 'completed', 'output': ping_command.execute()}