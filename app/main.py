from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host: str):
        self.host = host

    def run(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr}''

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host == 'localhost' or host == '127.0.0.1':  # Add validation for trusted hosts
        safe_ping_instance = SafePing(host)
        result = safe_ping_instance.run()
        return {"status": "completed", "result": result}
    else:
        return {"status": "error", "message": "Untrusted host"}