from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e}

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return {'status': 'completed', 'result': command.execute()}}