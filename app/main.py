from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            output = subprocess.run(['ping', subprocess.quote(self.host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(subprocess.quote(host))  # Sanitize input
    return safe_ping.run()