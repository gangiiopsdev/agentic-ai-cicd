from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def safe_ping(self):
        try:
            output = subprocess.run(['ping', '-c', '1', self.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance = SafePing(host)
    return safe_ping_instance.safe_ping()