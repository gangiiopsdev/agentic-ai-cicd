from fastapi import FastAPI
import subprocess
class PingHost:
    def __init__(self, host):
        self.host = host

    def execute_ping(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_host = PingHost(host)
    result = ping_host.execute_ping()
    return {
        'status': 'completed',
        'output': result.stdout,
        'stderr': result.stderr
    }