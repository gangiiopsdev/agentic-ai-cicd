from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']  # Define allowed hosts

    def execute(self, host):
        if host in self.allowed_hosts:
            try:
                output = subprocess.run(['ping', host], capture_output=True, text=True)
                return {'status': 'completed', 'output': output.stdout}
            except Exception as e:
                return {'status': 'error', 'message': str(e)}
        else:
            return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand().execute(host)