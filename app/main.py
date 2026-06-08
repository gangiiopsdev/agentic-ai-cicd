from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with list of arguments
        args = ['ping', '-c', '1', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

global_ping_host = PingHost('example.com')

app = FastAPI()

@app.get("/ping")
def ping():
    status = global_ping_host.execute()
    return {'status': 'completed', 'response': status}