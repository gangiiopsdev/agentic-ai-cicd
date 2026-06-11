from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            # Validate the input more strictly to avoid shell injection
            if not self.host.isalnum() or len(self.host) > 255:
                raise ValueError("Invalid host")
            # Using subprocess.run instead of subprocess.call for better control
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()