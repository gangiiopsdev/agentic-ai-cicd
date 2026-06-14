from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with proper quoting
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand(host='example.com')

    def ping(self):
        status = self.ping_command.execute()
        return {'status': 'completed', 'output': status}
app = FastAPI()

@app.get("/ping")
def ping():
    endpoint = PingEndpoint()
    return endpoint.ping()