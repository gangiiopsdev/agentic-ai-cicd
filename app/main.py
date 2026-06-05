from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            # Secure implementation using subprocess.run with shell=False and list parameters
            result = subprocess.run(['ping', '-c', '1', self.host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Create an instance of PingCommand and call its execute method
    command = PingCommand(host)
    return command.execute()