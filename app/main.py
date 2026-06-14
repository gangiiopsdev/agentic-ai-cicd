from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self, host: str):
        self.host = host

    def ping(self):
        # Secure implementation using subprocess.run with shell=False
        subprocess.run(['ping', '-c', '4', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler(host)
    handler.ping()
    return {"status": "completed"}