from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.command = ['ping']

    def ping(self, host: str):
        try:
            subprocess.run(self.command + [host], check=True)
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)