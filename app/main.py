from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

    def safe_ping(self, host):
        try:
            output = subprocess.run(self.ping_command + [host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.safe_ping(host)